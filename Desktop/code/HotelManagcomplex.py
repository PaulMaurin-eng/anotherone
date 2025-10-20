#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 13:45:46 2025

@author: paulmaurin
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date, timedelta, datetime
from typing import List, Dict, Optional, Tuple
from enum import Enum, auto


# =========================
#        ENUMS
# =========================

class RoomType(Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"


class ReservationStatus(Enum):
    PENDING = auto()
    CONFIRMED = auto()
    CANCELLED = auto()
    REFUNDED = auto()


class PaymentStatus(Enum):
    INITIATED = auto()
    PAID = auto()
    REFUNDED = auto()
    FAILED = auto()


# =========================
#        ROOMS
# =========================

class Room(ABC):
    """Abstract base for rooms with encapsulated attributes and polymorphic pricing."""
    def __init__(self, room_number: int, base_price_per_night: float):
        self._room_number = room_number                 # encapsulated id
        self._base_price_per_night = base_price_per_night  # encapsulated price

    @property
    def room_number(self) -> int:
        return self._room_number

    @property
    def base_price_per_night(self) -> float:
        return self._base_price_per_night

    @abstractmethod
    def room_type(self) -> RoomType:
        ...

    @abstractmethod
    def nightly_rate(self, when: date) -> float:
        """Polymorphic pricing (e.g., weekend/seasonal multipliers)."""
        ...

    def __str__(self) -> str:
        return f"{self.room_type().value} Room #{self.room_number} (base {self.base_price_per_night:.2f})"


class SingleRoom(Room):
    def room_type(self) -> RoomType:
        return RoomType.SINGLE

    def nightly_rate(self, when: date) -> float:
        # Weekend bump +10%
        weekend = when.weekday() >= 5
        return self.base_price_per_night * (1.10 if weekend else 1.00)


class DoubleRoom(Room):
    def room_type(self) -> RoomType:
        return RoomType.DOUBLE

    def nightly_rate(self, when: date) -> float:
        # Base +20% as spec + weekend +5%
        weekend = when.weekday() >= 5
        return self.base_price_per_night * 1.20 * (1.05 if weekend else 1.00)


class Suite(Room):
    def room_type(self) -> RoomType:
        return RoomType.SUITE

    def nightly_rate(self, when: date) -> float:
        # Base +50% as spec + high season (July–Aug) +15%
        high_season = when.month in (7, 8)
        return self.base_price_per_night * 1.50 * (1.15 if high_season else 1.00)


# =========================
#       GUEST & LOYALTY
# =========================

class LoyaltyTier(Enum):
    BRONZE = "Bronze"   # 0–999 pts → 0% discount
    SILVER = "Silver"   # 1000–2999 pts → 5% discount
    GOLD = "Gold"       # 3000+ pts → 10% discount


@dataclass
class Guest:
    name: str
    email: str
    _points: int = 0

    @property
    def points(self) -> int:
        return self._points

    @property
    def tier(self) -> LoyaltyTier:
        if self._points >= 3000:
            return LoyaltyTier.GOLD
        elif self._points >= 1000:
            return LoyaltyTier.SILVER
        return LoyaltyTier.BRONZE

    def add_points(self, amount_spent: float) -> None:
        # Earn 10 pts per $ spent (rounded)
        self._points += int(round(amount_spent * 10, 0))


# =========================
#      DISCOUNT STRATEGY
# =========================

class Discount(ABC):
    """Strategy interface."""
    @abstractmethod
    def apply(self, subtotal: float, context: dict) -> Tuple[str, float]:
        """Return (label, discount_amount) given a subtotal and context."""
        ...


class LoyaltyDiscount(Discount):
    def apply(self, subtotal: float, context: dict) -> Tuple[str, float]:
        tier: LoyaltyTier = context["guest"].tier
        pct = 0.0
        if tier == LoyaltyTier.SILVER:
            pct = 0.05
        elif tier == LoyaltyTier.GOLD:
            pct = 0.10
        return (f"Loyalty ({tier.value})", subtotal * pct)


class PromoCodeDiscount(Discount):
    def __init__(self, code_to_pct: Dict[str, float]):
        self.code_to_pct = code_to_pct

    def apply(self, subtotal: float, context: dict) -> Tuple[str, float]:
        code = context.get("promo_code")
        if not code:
            return ("Promo (none)", 0.0)
        pct = self.code_to_pct.get(code.upper(), 0.0)
        return (f"Promo ({code.upper()})", subtotal * pct)


class LongStayDiscount(Discount):
    def apply(self, subtotal: float, context: dict) -> Tuple[str, float]:
        nights = context["nights"]
        # 7+ nights → 8% discount
        return ("Long Stay (7+ nights)" , subtotal * 0.08) if nights >= 7 else ("Long Stay", 0.0)


# =========================
#          INVOICE
# =========================

@dataclass
class LineItem:
    label: str
    amount: float


@dataclass
class Invoice:
    line_items: List[LineItem] = field(default_factory=list)
    discounts: List[LineItem] = field(default_factory=list)
    tax_rate: float = 0.16  # 16% VAT (MX style)
    fees: List[LineItem] = field(default_factory=list)

    def add_line(self, label: str, amount: float) -> None:
        self.line_items.append(LineItem(label, amount))

    def add_fee(self, label: str, amount: float) -> None:
        self.fees.append(LineItem(label, amount))

    def add_discount(self, label: str, amount: float) -> None:
        # amount should be positive; we will subtract it
        self.discounts.append(LineItem(label, amount))

    @property
    def subtotal(self) -> float:
        return sum(x.amount for x in self.line_items)

    @property
    def total_fees(self) -> float:
        return sum(f.amount for f in self.fees)

    @property
    def total_discounts(self) -> float:
        return sum(d.amount for d in self.discounts)

    @property
    def taxable_amount(self) -> float:
        return max(0.0, self.subtotal + self.total_fees - self.total_discounts)

    @property
    def tax(self) -> float:
        return round(self.taxable_amount * self.tax_rate, 2)

    @property
    def total(self) -> float:
        return round(self.taxable_amount + self.tax, 2)

    def summary(self) -> str:
        lines = ["--- Invoice ---"]
        for li in self.line_items:
            lines.append(f"{li.label:<30} ${li.amount:>8.2f}")
        if self.fees:
            for f in self.fees:
                lines.append(f"{f.label:<30} ${f.amount:>8.2f}")
        if self.discounts:
            for d in self.discounts:
                lines.append(f"{d.label:<30} -${d.amount:>7.2f}")
        lines.append(f"{'Subtotal':<30} ${self.subtotal:>8.2f}")
        lines.append(f"{'Tax':<30} ${self.tax:>8.2f}")
        lines.append(f"{'TOTAL':<30} ${self.total:>8.2f}")
        return "\n".join(lines)


# =========================
#           PAYMENTS
# =========================

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> PaymentStatus:
        ...

    @abstractmethod
    def refund(self, amount: float) -> PaymentStatus:
        ...


class CashPayment(Payment):
    def pay(self, amount: float) -> PaymentStatus:
        print(f"[Cash] Collected ${amount:.2f}")
        return PaymentStatus.PAID

    def refund(self, amount: float) -> PaymentStatus:
        print(f"[Cash] Refund handed out: ${amount:.2f}")
        return PaymentStatus.REFUNDED


class CreditCardPayment(Payment):
    def __init__(self, card_last4: str):
        self.card_last4 = card_last4

    def pay(self, amount: float) -> PaymentStatus:
        print(f"[Card ****{self.card_last4}] Charged ${amount:.2f}")
        return PaymentStatus.PAID

    def refund(self, amount: float) -> PaymentStatus:
        print(f"[Card ****{self.card_last4}] Refunded ${amount:.2f}")
        return PaymentStatus.REFUNDED


class PayPalPayment(Payment):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> PaymentStatus:
        print(f"[PayPal {self.email}] Paid ${amount:.2f}")
        return PaymentStatus.PAID

    def refund(self, amount: float) -> PaymentStatus:
        print(f"[PayPal {self.email}] Refunded ${amount:.2f}")
        return PaymentStatus.REFUNDED


# =========================
#         LEDGER
# =========================

@dataclass
class Transaction:
    timestamp: datetime
    reservation_id: str
    type: str  # "CHARGE" | "REFUND" | "CANCELLATION_FEE"
    amount: float
    method: str


class Ledger:
    def __init__(self):
        self._entries: List[Transaction] = []

    def record(self, tx: Transaction) -> None:
        self._entries.append(tx)

    def all(self) -> List[Transaction]:
        return list(self._entries)

    def revenue(self, start: Optional[date] = None, end: Optional[date] = None) -> float:
        total = 0.0
        for t in self._entries:
            d = t.timestamp.date()
            if (start is None or d >= start) and (end is None or d <= end):
                # charges positive, refunds negative
                if t.type in ("CHARGE", "CANCELLATION_FEE"):
                    total += t.amount
                elif t.type == "REFUND":
                    total -= t.amount
        return round(total, 2)


# =========================
#     AVAILABILITY CAL
# =========================

def daterange(start: date, end: date):
    """Yield each night from start to end (end is check-out, non-inclusive)."""
    d = start
    while d < end:
        yield d
        d += timedelta(days=1)


class BookingCalendar:
    """Tracks booked nights per room_number to prevent overlaps."""
    def __init__(self):
        self._booked: Dict[int, List[Tuple[date, date]]] = {}

    def is_available(self, room_number: int, check_in: date, check_out: date) -> bool:
        if check_out <= check_in:
            return False
        periods = self._booked.get(room_number, [])
        for (s, e) in periods:
            if not (check_out <= s or e <= check_in):  # overlap
                return False
        return True

    def book(self, room_number: int, check_in: date, check_out: date) -> bool:
        if not self.is_available(room_number, check_in, check_out):
            return False
        self._booked.setdefault(room_number, []).append((check_in, check_out))
        return True

    def cancel(self, room_number: int, check_in: date, check_out: date) -> None:
        periods = self._booked.get(room_number, [])
        if periods:
            try:
                periods.remove((check_in, check_out))
            except ValueError:
                pass  # not found; ignore for safety


# =========================
#       RESERVATIONS
# =========================

@dataclass
class Reservation:
    reservation_id: str
    guest: Guest
    room: Room
    check_in: date
    check_out: date
    nights: int
    status: ReservationStatus = ReservationStatus.PENDING
    invoice: Optional[Invoice] = None
    promo_code: Optional[str] = None

    def span(self) -> Tuple[date, date]:
        return (self.check_in, self.check_out)


class CancellationPolicy:
    """Encapsulates how refunds/cancellation fees are computed."""
    def __init__(self, free_cancel_days: int = 3, late_fee_nights: int = 1):
        self.free_cancel_days = free_cancel_days
        self.late_fee_nights = late_fee_nights

    def fee(self, today: date, reservation: Reservation) -> float:
        days_before = (reservation.check_in - today).days
        if days_before >= self.free_cancel_days:
            return 0.0
        # Late cancellation → charge X nights at room *average* nightly rate
        # For simplicity, average over booked nights:
        nightly_rates = [reservation.room.nightly_rate(d) for d in daterange(reservation.check_in, reservation.check_out)]
        avg = sum(nightly_rates) / max(1, len(nightly_rates))
        return round(avg * self.late_fee_nights, 2)


# =========================
#           HOTEL
# =========================

class Hotel:
    def __init__(self, name: str, tax_rate: float = 0.16):
        self.name = name
        self._rooms: Dict[int, Room] = {}
        self._calendar = BookingCalendar()
        self._ledger = Ledger()
        self._tax_rate = tax_rate
        # discount strategies (compose/chain)
        self._discounts: List[Discount] = [
            LoyaltyDiscount(),
            PromoCodeDiscount({"WELCOME10": 0.10, "FALL5": 0.05}),
            LongStayDiscount(),
        ]
        self._cancel_policy = CancellationPolicy()

    # ---- Rooms management
    def add_room(self, room: Room) -> None:
        self._rooms[room.room_number] = room

    def rooms(self) -> List[Room]:
        return list(self._rooms.values())

    # ---- Search
    def available_rooms(self, room_type: Optional[RoomType], check_in: date, check_out: date) -> List[Room]:
        out = []
        for r in self._rooms.values():
            if room_type and r.room_type() != room_type:
                continue
            if self._calendar.is_available(r.room_number, check_in, check_out):
                out.append(r)
        return out

    # ---- Pricing / Invoice
    def _generate_invoice(self, guest: Guest, room: Room, check_in: date, check_out: date, promo_code: Optional[str]) -> Invoice:
        inv = Invoice(tax_rate=self._tax_rate)
        nights = (check_out - check_in).days
        # nightly lines
        for d in daterange(check_in, check_out):
            inv.add_line(f"{room.room_type().value} {room.room_number} @ {d.isoformat()}", room.nightly_rate(d))
        # fees (example)
        inv.add_fee("Service Fee", 12.00)
        inv.add_fee("City Fee", 3.50)
        # discounts chain
        context = {"guest": guest, "nights": nights, "promo_code": promo_code}
        for strat in self._discounts:
            label, disc = strat.apply(inv.subtotal + inv.total_fees - inv.total_discounts, context)
            if disc > 0:
                inv.add_discount(label, round(disc, 2))
        return inv

    # ---- Book
    def book(self, guest: Guest, room_number: int, check_in: date, check_out: date, payment: Payment, promo_code: Optional[str] = None) -> Reservation:
        if room_number not in self._rooms:
            raise ValueError("Room does not exist.")
        room = self._rooms[room_number]
        if not self._calendar.book(room_number, check_in, check_out):
            raise ValueError("Room not available for those dates.")
        rid = f"R-{room_number}-{int(datetime.now().timestamp())}"
        res = Reservation(
            reservation_id=rid,
            guest=guest,
            room=room,
            check_in=check_in,
            check_out=check_out,
            nights=(check_out - check_in).days,
            status=ReservationStatus.PENDING,
            promo_code=promo_code
        )
        inv = self._generate_invoice(guest, room, check_in, check_out, promo_code)
        res.invoice = inv

        # charge
        status = payment.pay(inv.total)
        if status == PaymentStatus.PAID:
            res.status = ReservationStatus.CONFIRMED
            self._ledger.record(Transaction(datetime.now(), res.reservation_id, "CHARGE", inv.total, payment.__class__.__name__))
            guest.add_points(inv.total)  # loyalty points
            print(f"[{self.name}] Booking CONFIRMED: {res.reservation_id} for {guest.name}")
        else:
            # unbook calendar if failed
            self._calendar.cancel(room_number, check_in, check_out)
            res.status = ReservationStatus.PENDING
            print(f"[{self.name}] Payment failed; reservation not confirmed.")

        return res

    # ---- Cancel
    def cancel(self, reservation: Reservation, today: Optional[date] = None, payment: Optional[Payment] = None) -> float:
        if reservation.status not in (ReservationStatus.CONFIRMED, ReservationStatus.PENDING):
            print("Cannot cancel; reservation already cancelled/refunded.")
            return 0.0

        today = today or date.today()
        fee = self._cancel_policy.fee(today, reservation)

        # release calendar
        self._calendar.cancel(reservation.room.room_number, reservation.check_in, reservation.check_out)
        reservation.status = ReservationStatus.CANCELLED

        # compute refund: full paid - fee
        paid = reservation.invoice.total if reservation.invoice else 0.0
        refund_amount = max(0.0, paid - fee)

        if refund_amount > 0 and payment is not None:
            payment.refund(refund_amount)
            self._ledger.record(Transaction(datetime.now(), reservation.reservation_id, "REFUND", refund_amount, payment.__class__.__name__))
            reservation.status = ReservationStatus.REFUNDED

        if fee > 0:
            self._ledger.record(Transaction(datetime.now(), reservation.reservation_id, "CANCELLATION_FEE", fee, "CancellationPolicy"))

        print(f"[{self.name}] Reservation {reservation.reservation_id} cancelled. Fee: ${fee:.2f}, Refund: ${refund_amount:.2f}")
        return refund_amount

    # ---- Admin reports
    def occupancy_rate(self, start: date, end: date) -> float:
        """Simple occupancy: total booked room-nights / (rooms * nights)."""
        total_room_nights = len(self._rooms) * max(0, (end - start).days)
        if total_room_nights == 0:
            return 0.0

        # approximate via booked ranges
        booked = 0
        for r in self._rooms.values():
            # naive: scan each night and check availability
            for d in daterange(start, end):
                if not self._calendar.is_available(r.room_number, d, d + timedelta(days=1)):
                    booked += 1
        return round(100 * booked / total_room_nights, 2)

    def revenue(self, start: Optional[date] = None, end: Optional[date] = None) -> float:
        return self._ledger.revenue(start, end)

    def list_available(self, start: date, end: date) -> str:
        rows = [f"--- Available Rooms {start.isoformat()} → {end.isoformat()} ---"]
        for rt in RoomType:
            rooms = self.available_rooms(rt, start, end)
            label = ", ".join(str(r.room_number) for r in rooms) or "None"
            rows.append(f"{rt.value:<8}: {label}")
        return "\n".join(rows)

    def print_ledger(self) -> str:
        lines = ["--- Ledger ---"]
        for t in self._ledger.all():
            lines.append(f"{t.timestamp.isoformat(timespec='seconds')} | {t.reservation_id} | {t.type:<16} ${t.amount:>7.2f} | {t.method}")
        return "\n".join(lines)


# =========================
#        DEMO / TEST
# =========================

if __name__ == "__main__":
    # Setup hotel inventory
    hotel = Hotel("Azul Reforma", tax_rate=0.16)
    hotel.add_room(SingleRoom(101, 100))
    hotel.add_room(SingleRoom(102, 100))
    hotel.add_room(DoubleRoom(201, 150))
    hotel.add_room(Suite(301, 300))

    # Guests
    paul = Guest("Paul", "paul@email.com")
    jean = Guest("Jean", "jean@email.com")

    # Dates
    today = date.today()
    next_fri = today + timedelta(days=(4 - today.weekday()) % 7)  # upcoming Friday
    next_sun = next_fri + timedelta(days=2)
    long_stay_start = today + timedelta(days=10)
    long_stay_end = long_stay_start + timedelta(days=8)  # 8 nights → long stay

    # Admin view
    print(hotel.list_available(next_fri, next_sun))

    # Bookings
    print("\n-- Booking 1 (Paul, SingleRoom, weekend, promo WELCOME10, credit card) --")
    r1 = hotel.book(
        guest=paul,
        room_number=101,
        check_in=next_fri,
        check_out=next_sun,
        payment=CreditCardPayment("1234"),
        promo_code="WELCOME10"
    )
    print(r1.invoice.summary())
    print(f"Paul tier: {paul.tier.value}, points: {paul.points}")

    # Attempt overlapping booking on same room should fail
    print("\n-- Attempt overlapping on same room (should fail) --")
    try:
        hotel.book(jean, 101, next_fri, next_sun, PayPalPayment("jean@paypal.com"))
    except ValueError as e:
        print("Expected error:", e)

    # Book suite for long stay to trigger long-stay discount; pay with PayPal
    print("\n-- Booking 2 (Jean, Suite 8 nights, no promo, PayPal) --")
    r2 = hotel.book(
        guest=jean,
        room_number=301,
        check_in=long_stay_start,
        check_out=long_stay_end,
        payment=PayPalPayment("jean@paypal.com")
    )
    print(r2.invoice.summary())
    print(f"Jean tier: {jean.tier.value}, points: {jean.points}")

    # Cancel Jean late (simulate today close to check-in to trigger fee)
    print("\n-- Cancellation (late) for Jean --")
    late_today = long_stay_start - timedelta(days=1)
    refund = hotel.cancel(r2, today=late_today, payment=PayPalPayment("jean@paypal.com"))
    print(f"Refund processed: ${refund:.2f}")

    # Admin dashboard
    print("\n-- Admin Dashboard --")
    span_start = today
    span_end = today + timedelta(days=30)
    print(hotel.list_available(span_start, span_end))
    print(f"Occupancy next 30d: {hotel.occupancy_rate(span_start, span_end)}%")
    print(f"Revenue next 30d: ${hotel.revenue(span_start, span_end):.2f}")
    print(hotel.print_ledger())

# 🍜 Boat & Go — Thai Boat Noodle Pre-Order App

**ICMB150 Group Project — Anvil Web Application**

## About
Boat & Go is a web-based pre-order application for a local Thai boat noodle shop.
Customers can browse the menu, customise their bowl, and place a pickup order —
eliminating long queues and reducing order mix-ups.

## App Structure

| Form | Description |
|------|-------------|
| `HomeScreen` | Role selection — Customer, Staff, or Owner |
| `CustomerMenu` | Menu grid with all available bowls |
| `CustomerOrder` | Order form — name, noodle type, spice, pickup time, payment |
| `CustomerStatus` | 3-stage order tracker + QR code + payment status badge |
| `OwnerLogin` | PIN code login for owner access |
| `OwnerDashboard` | Today's date, revenue summary, full order list |
| `StaffDashboard` | Simplified order queue for kitchen staff |

## How to Clone into Anvil

1. Go to [anvil.works](https://anvil.works)
2. Click **"New App"**
3. Choose **"Clone from GitHub"**
4. Paste this repository URL
5. Click **Clone** — the app will open ready to run

## Default Owner PIN
`1234` — change this in `OwnerLogin/__init__.py` line 5

## Team Members
| ID | Name | Contribution |
|----|------|-------------|
| ___ | ___ | HomeScreen + Navigation |
| ___ | ___ | CustomerMenu + CustomerOrder |
| ___ | ___ | CustomerStatus + OwnerLogin |
| ___ | ___ | OwnerDashboard + StaffDashboard |

## Built With
- [Anvil](https://anvil.works) — Python web app framework
- Python 3

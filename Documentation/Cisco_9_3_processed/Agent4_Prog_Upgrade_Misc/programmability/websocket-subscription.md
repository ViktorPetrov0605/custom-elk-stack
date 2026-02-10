# WebSocket Subscription

**Source:** m-n9k-websocket-subscription-93x.html

**Tags:** websocket, telemetry, subscription, nx-api, real-time, notifications, streaming

**Updated:** September 11, 2023

---

## Overview

Cisco NX-OS provides an interface capability to enable the switch to push notifications to interested subscribers. Through the NX-API WebSocket interface, programs and end-users can receive notifications about various state changes on the switch, eliminating the need for periodic polling.

When you perform an API query using the Cisco NX-API REST interface, you have the option to create a subscription to any future changes in the results of a given query. When any management object (MO) is created, changed, or deleted, because of a user-initiated or system-initiated action, an event is generated. If the received event changes the results of a subscribed query, the switch generates a push notification to the API client that created the subscription.

---

## Opening a WebSocket

The API subscription feature uses the WebSocket protocol (RFC 6455) to implement a two-way connection with the API client. This way, the API can send unsolicited notification messages to the client itself. To establish the notification channel, you must first open a WebSocket connection with the respective API. Only a single WebSocket connection is needed to support multiple query subscriptions within each switch. The WebSocket connection is dependent on your API session connection (via token validation), and closes when your API session ends.

### Python Example

```python
from websocket import create_connection

connection_string = "ws://10.1.2.3/socket{0}".format(token)
ws = create_connection(connection_string, sslopt={"check_hostname": False})
```

### URI Format

```
ws://10.1.2.3/socket<token>
```

Example:
```
ws://10.1.2.3/socketGkZl5NLRZJl5+jqChouaZ9CYjgE58W/pMccR+LeXmdO0obG9NBIwo1VBo7+YC1oiJL9mS6I9qh62BkX+Xddhe0JYrTmSG4JcKZ4t3bcP2Mxy3VBmgoJjwZ76ZOuf9V9AD6Xl83lyoR4bLBzqbSSU1R2NIgUotCGWjZt5JX6CJF0=
```

---

## Creating a Subscription

To create a subscription to a query, perform the query with the option `?subscription=yes`.

### Example Request

```
GET http://10.1.1.1/api/mo/sys/intf/phys-[eth1/1].json?subscription=yes
```

### Response with Subscription ID

```json
{
  "totalCount": "0",
  "subscriptionId": "18374686685813276673",
  "imdata": []
}
```

The query response contains a subscription identifier (`subscriptionId`) that you can use to refresh the subscription and identify future notifications from the given subscription.

---

## Receiving Notifications

An event notification from the subscription delivers a data structure that contains the subscription ID and the MO description.

### Notification Example (JSON)

```json
{
  "subscriptionId": ["18374686685813276673"],
  "imdata": [{
    "l1PhysIf": {
      "attributes": {
        "childAction": "",
        "descr": "test",
        "dn": "sys/intf/phys-[eth1/1]",
        "modTs": "2019-10-18T19:42:29.446+00:00",
        "rn": "",
        "status": "modified"
      }
    }
  }]
}
```

As multiple active subscriptions can exist for a given query, a notification can contain multiple subscription IDs. Notifications are supported in either JSON or XML format.

---

## Refreshing the Subscription

Subscriptions require periodic refreshing to remain active. If not refreshed, the subscription will expire.

---

## Closing the WebSocket

The WebSocket connection closes automatically when:
- The API session ends
- The connection is explicitly closed by the client
- Network connectivity is lost

---

## Part of

- [Programmability Guide - Main TOC](programmability-guide-93x.md)

---

*This chapter is part of the Cisco Nexus 9000 Series NX-OS Programmability Guide, Release 9.3(x)*

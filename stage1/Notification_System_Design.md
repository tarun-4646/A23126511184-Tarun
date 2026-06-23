# Priority Notification Engine

## Objective

Display Top 10 highest priority notifications.

## Priority Order

1. Placement
2. Result
3. Event

## Sorting Rules

- Higher priority first
- Latest timestamp first

## Algorithm

1. Read notifications from JSON.
2. Assign priority weights.
3. Convert timestamps.
4. Sort notifications.
5. Return Top 10 notifications.

## Time Complexity

O(n log n)

## Space Complexity

O(n)
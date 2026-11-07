# Ticket

A printed ferry, bus or event ticket with a perforated stub. `torn` removes the stub and leaves a ragged edge: the other half is somewhere else, which is often the point.

- `operator` (fictional), `from`, `to`, `date`, `time`, `fare`, `serial`, `torn`.
- Fields default to Date, Sailing and Fare, and the stub to Adult. For a bus or event, pass `labels: { date, time, fare }` ("Departs", "Doors") and `passenger` ("Child", "General admission").
- The torn edge is an irregular rip, not a perforation. Use `torn` when the other half matters to the story.
- Wrap in `Evidence`.

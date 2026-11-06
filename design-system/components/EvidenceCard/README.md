# EvidenceCard

A piece of evidence: a pinned `manila` card with `shadow-card`, which reads the same in both themes because it's an object on the table.

- `number` is shown zero-padded in mono ("Evidence 04"). `title` is set in serif and `location` sits under a dashed tear line.
- `status`: `new` (just recovered), `found` (already read, slightly faded), `locked` (text blurred and hidden from screen readers until the team reaches the location).
- Body text is the evidence itself: two or three short, factual sentences. See the voice rules in the README.
- In a sequence, connect cards with the red thread from pin to pin (one thread, see the thread rule).
- Consumer provides: `title`, the evidence text (children), and optionally `number`, `status` and `location`.

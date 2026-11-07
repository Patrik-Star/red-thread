import type * as React from 'react';

/* ---------- Game layer: rounded, flat, off-white ---------- */

export interface WordmarkProps { size?: 'sm' | 'md' | 'lg'; className?: string }
/** Provisional "Red Thread" lockup: serif name with one thread passing under it, tied off at a brass pin. */
export declare function Wordmark(props: WordmarkProps): React.ReactElement;

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** primary = thread fill, once per screen. ghost = outlined, everything else. */
  variant?: 'primary' | 'ghost';
  size?: 'md' | 'sm';
}
export declare function Button(props: ButtonProps): React.ReactElement;

export interface CaseTagProps { tone?: 'open' | 'solved' | 'neutral'; children?: React.ReactNode; className?: string }
export declare function CaseTag(props: CaseTagProps): React.ReactElement;

export interface ThreadDividerProps { label?: React.ReactNode; className?: string }
export declare function ThreadDivider(props: ThreadDividerProps): React.ReactElement;

export interface GameNoteProps {
  /** instruction (default), hint (dashed edge), unlock (adds code cells). */
  kind?: 'instruction' | 'hint' | 'unlock';
  title?: React.ReactNode;
  /** Mono footer, left and right: stop number, walking time, hint cost. */
  meta?: React.ReactNode;
  metaEnd?: React.ReactNode;
  codeLength?: number;
  numeric?: boolean;
  codeLabel?: string;
  codeMessage?: React.ReactNode;
  /** wrong thickens the cell borders; right locks the cells. The message carries the words, never red. */
  codeState?: 'wrong' | 'right';
  onCode?: (value: string) => void;
  disabled?: boolean;
  ariaLabel?: string;
  children?: React.ReactNode;
  className?: string;
}
export declare function GameNote(props: GameNoteProps): React.ReactElement;

/* ---------- The join: manila tag + object ---------- */

export type EvidenceStatus = 'new' | 'found' | 'locked';

export interface EvidenceTagProps { number?: number; status?: EvidenceStatus; title?: React.ReactNode; found?: React.ReactNode }
export declare function EvidenceTag(props: EvidenceTagProps): React.ReactElement;

export interface EvidenceProps extends EvidenceTagProps {
  /** Text for the GameNote laid over a locked object. While locked, pass a decoy child: the blur is a look, not a lock. */
  lockedText?: React.ReactNode;
  /** Set when the child is a PhoneScreenshot (it carries its own shadow). */
  device?: boolean;
  /** Screen-reader description of the object. */
  caption?: string;
  children: React.ReactNode;
  className?: string;
}
export declare function Evidence(props: EvidenceProps): React.ReactElement;

/* ---------- Story layer: square, white, shadowed. "[redacted]" in any string prints a black bar. ---------- */

export interface ReceiptProps {
  /** Printed above the merchant, e.g. "Tax invoice". */
  heading?: string;
  merchant: string; address?: string; gstNumber?: string; date: string; time: string;
  /** Table or docket number. (Not `ref`, which React reserves.) */
  serial?: string; server?: string;
  lines: { qty?: number; item: string; price: string }[];
  subtotal?: string;
  /** Leave out and no TOTAL line prints. */
  total?: string; gst?: string; paid?: string; tendered?: string; card?: string; footer?: string; stamp?: string;
  /** EFTPOS slip lines: [['Acct', 'Credit'], ['Auth', '[redacted]']]. */
  extra?: [string, string?][];
}
export declare function Receipt(props: ReceiptProps): React.ReactElement;

export type Message = { from: 'them' | 'me'; text: string } | { day: string } | { receipt: string };
export interface PhoneScreenshotProps {
  app?: 'messages' | 'calls';
  time?: string; battery?: number; contact?: string;
  messages?: Message[];
  calls?: { name: string; time: string; missed?: boolean; kind?: string; duration?: string }[];
  /** Accessible label; defaults to "Screenshot of a phone: messages with …". */
  label?: string;
  /** Custom screen content instead of messages/calls. */
  children?: React.ReactNode;
}
export declare function PhoneScreenshot(props: PhoneScreenshotProps): React.ReactElement;

export interface PhoneRecordsProps {
  carrier: string; holder?: string; number?: string; period?: string; footer?: string;
  rows: { date: string; time: string; dir: 'out' | 'in' | 'missed' | 'sms' | 'sms-in'; to: string; duration?: string; marked?: boolean }[];
}
export declare function PhoneRecords(props: PhoneRecordsProps): React.ReactElement;

export interface BankStatementProps {
  bank: string; holder?: string; account?: string; period?: string; footer?: string;
  rows: { date: string; details: string; out?: string; in?: string; balance?: string; marked?: boolean }[];
}
export declare function BankStatement(props: BankStatementProps): React.ReactElement;

export interface TicketProps {
  operator: string; from: string; to: string; date: string; time: string; fare: string; serial?: string; torn?: boolean;
  /** Field labels; defaults Date / Sailing / Fare. */
  labels?: { date?: string; time?: string; fare?: string };
  /** Stub label; default "Adult". */
  passenger?: string;
}
export declare function Ticket(props: TicketProps): React.ReactElement;

export interface HandwrittenNoteProps { lines?: string[]; signed?: string; paper?: 'lined' | 'plain'; children?: React.ReactNode }
export declare function HandwrittenNote(props: HandwrittenNoteProps): React.ReactElement;

export interface CctvStillProps {
  src?: string; alt?: string; camera?: string; place?: string; date?: string; timestamp?: string;
  /** Production placeholder text, shown in a dashed frame when there is no src. Never ship to players. */
  slot?: string;
}

export interface PrintoutProps {
  org: string; title?: string; info?: [string, string][];
  columns: { label: string; align?: 'right'; wrap?: boolean }[];
  rows: (string[] | { cells: string[]; marked?: boolean })[];
  footer?: string;
}
/** Any other printed log: taxi trips, door swipes, inventories. */
export declare function Printout(props: PrintoutProps): React.ReactElement;
export declare function CctvStill(props: CctvStillProps): React.ReactElement;

declare global {
  interface Window {
    RedThread: {
      Wordmark: typeof Wordmark; Button: typeof Button; CaseTag: typeof CaseTag; ThreadDivider: typeof ThreadDivider;
      GameNote: typeof GameNote; Evidence: typeof Evidence; EvidenceTag: typeof EvidenceTag;
      Receipt: typeof Receipt; PhoneScreenshot: typeof PhoneScreenshot; PhoneRecords: typeof PhoneRecords;
      BankStatement: typeof BankStatement; Ticket: typeof Ticket; HandwrittenNote: typeof HandwrittenNote; CctvStill: typeof CctvStill; Printout: typeof Printout;
    };
  }
}

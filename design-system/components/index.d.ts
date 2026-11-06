import type * as React from 'react';

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

export interface EvidenceCardProps {
  number?: number;
  title: React.ReactNode;
  /** new: just recovered. found: already read. locked: text blurred until the team reaches the location. */
  status?: 'new' | 'found' | 'locked';
  location?: React.ReactNode;
  children?: React.ReactNode;
  className?: string;
}
export declare function EvidenceCard(props: EvidenceCardProps): React.ReactElement;

export interface ThreadDividerProps { label?: React.ReactNode; className?: string }
export declare function ThreadDivider(props: ThreadDividerProps): React.ReactElement;

declare global {
  interface Window {
    RedThread: { Wordmark: typeof Wordmark; Button: typeof Button; CaseTag: typeof CaseTag; EvidenceCard: typeof EvidenceCard; ThreadDivider: typeof ThreadDivider };
  }
}

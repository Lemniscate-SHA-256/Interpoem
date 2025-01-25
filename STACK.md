Hybrid Syntax: Markdown-Like + Custom Tags

----------------------------------------------------------------

Parsing Tools
Regex for Simplicity: Start with regex to parse tags like <<set>>, <<if>>, and [[media]].

Zustand for State Management: Track variables ($mood) and passage navigation.

React Components for Media/Delays: Map [[image]], [[delay]] to React components (e.g., <TimedDelay ms={3000} />).

----------------------------------------------------------------

Key Libraries
Remark (Markdown Parser): Extend Markdown to support your custom syntax.

Zustand: Lightweight state management for variables and choices.

React-Player: For embedding audio/video ([[audio src="url"]]).
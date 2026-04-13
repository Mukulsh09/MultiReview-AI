import { useState } from 'react'

const severityStyles = {
  critical: 'bg-red-100 text-red-700',
  warning: 'bg-yellow-100 text-yellow-700',
  info: 'bg-blue-100 text-blue-700',
}

export default function IssueItem({ issue }) {
  const [expanded, setExpanded] = useState(false)

  return (
    <div className="border border-gray-100 rounded-lg p-3 mb-2">
      <div className="flex items-start gap-3">
        <span className={`text-xs font-medium px-2 py-1 rounded-full shrink-0 ${severityStyles[issue.severity]}`}>
          {issue.severity}
        </span>
        <div className="flex-1">
          <div className="flex items-center gap-2">
            <span className="text-xs text-gray-400 font-mono">Line {issue.line}</span>
          </div>
          <p className="text-sm text-gray-700 mt-1">{issue.message}</p>
          <button
            onClick={() => setExpanded(!expanded)}
            className="text-xs text-blue-600 hover:underline mt-1"
          >
            {expanded ? 'Hide suggestion ▲' : 'View suggestion ▼'}
          </button>
          {expanded && (
            <pre className="mt-2 bg-gray-900 text-green-400 text-xs rounded-md p-3 overflow-x-auto whitespace-pre-wrap">
              {issue.suggestion}
            </pre>
          )}
        </div>
      </div>
    </div>
  )
}
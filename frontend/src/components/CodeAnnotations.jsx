import { useState } from 'react'

const severityColors = {
  critical: { bg: 'bg-red-50', dot: 'bg-red-500', border: 'border-l-4 border-red-400' },
  warning: { bg: 'bg-yellow-50', dot: 'bg-yellow-400', border: 'border-l-4 border-yellow-400' },
  info: { bg: 'bg-blue-50', dot: 'bg-blue-400', border: 'border-l-4 border-blue-400' },
}

export default function CodeAnnotations({ code, agents }) {
  const [tooltip, setTooltip] = useState(null)

  const issuesByLine = {}
  agents.forEach(agent => {
    agent.issues.forEach(issue => {
      if (!issuesByLine[issue.line]) issuesByLine[issue.line] = []
      issuesByLine[issue.line].push(issue)
    })
  })

  const lines = code.split('\n')

  const topSeverity = (issues) => {
    if (issues.some(i => i.severity === 'critical')) return 'critical'
    if (issues.some(i => i.severity === 'warning')) return 'warning'
    return 'info'
  }

  return (
    <div className="bg-white rounded-lg border border-gray-200 mt-6 overflow-hidden">
      <div className="bg-gray-50 px-4 py-2 border-b border-gray-200">
        <span className="text-sm font-medium text-gray-600">Code Annotations</span>
        <span className="text-xs text-gray-400 ml-2">hover over highlighted lines to see issues</span>
      </div>

      <div className="relative font-mono text-sm overflow-x-auto">
        {lines.map((line, i) => {
          const lineNum = i + 1
          const issues = issuesByLine[lineNum]
          const severity = issues ? topSeverity(issues) : null
          const colors = severity ? severityColors[severity] : null

          return (
            <div
              key={i}
              className={`flex group relative ${colors ? colors.bg + ' ' + colors.border : ''}`}
              onMouseEnter={() => issues && setTooltip(lineNum)}
              onMouseLeave={() => setTooltip(null)}
            >
              <span className="w-10 text-right text-gray-400 text-xs py-1 px-2 select-none shrink-0 border-r border-gray-100">
                {lineNum}
              </span>

              <div className="flex items-center px-1 w-4 shrink-0">
                {issues && (
                  <span className={`w-2 h-2 rounded-full ${colors.dot}`} />
                )}
              </div>

              <pre className="py-1 px-2 flex-1 whitespace-pre text-gray-800">{line || ' '}</pre>

              {tooltip === lineNum && issues && (
                <div className="absolute left-16 top-full z-10 bg-gray-900 text-white text-xs rounded-lg p-3 shadow-xl w-80 mt-1">
                  {issues.map((issue, j) => (
                    <div key={j} className={j > 0 ? 'mt-2 pt-2 border-t border-gray-700' : ''}>
                      <span className={`text-xs font-semibold uppercase ${
                        issue.severity === 'critical' ? 'text-red-400' :
                        issue.severity === 'warning' ? 'text-yellow-400' : 'text-blue-400'
                      }`}>{issue.severity}</span>
                      <p className="mt-1 text-gray-200">{issue.message}</p>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
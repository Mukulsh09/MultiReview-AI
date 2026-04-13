export default function SummaryPanel({ summary, agents }) {
  const totalTime = agents.reduce((sum, a) => sum + a.response_time_ms, 0)

  const stats = [
    { label: 'Total Issues', value: summary.total_issues, color: 'bg-gray-100 text-gray-800' },
    { label: 'Critical', value: summary.critical, color: 'bg-red-100 text-red-700' },
    { label: 'Warning', value: summary.warning, color: 'bg-yellow-100 text-yellow-700' },
    { label: 'Info', value: summary.info, color: 'bg-blue-100 text-blue-700' },
  ]

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4 mt-6">
      <div className="flex items-center justify-between mb-3">
        <h2 className="text-sm font-semibold text-gray-700">Review Summary</h2>
        <span className="text-xs text-gray-400">Total time: {(totalTime / 1000).toFixed(1)}s</span>
      </div>
      <div className="grid grid-cols-4 gap-3">
        {stats.map(stat => (
          <div key={stat.label} className={`rounded-lg p-3 text-center ${stat.color}`}>
            <div className="text-2xl font-semibold">{stat.value}</div>
            <div className="text-xs mt-1">{stat.label}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
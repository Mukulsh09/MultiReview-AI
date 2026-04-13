import IssueItem from './IssueItem'

export default function AgentCard({ agent }) {
  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4">
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center gap-2">
          <h3 className="font-semibold text-gray-800 capitalize">{agent.name}</h3>
          <span className="text-xs bg-purple-100 text-purple-700 px-2 py-0.5 rounded-full">
            {agent.model}
          </span>
        </div>
        <div className="flex items-center gap-3 text-xs text-gray-400">
          <span>{agent.response_time_ms}ms</span>
          <span>{agent.issues.length} issue{agent.issues.length !== 1 ? 's' : ''}</span>
        </div>
      </div>

      {agent.issues.length === 0 ? (
        <p className="text-sm text-green-600">✓ No issues found</p>
      ) : (
        agent.issues.map((issue, i) => <IssueItem key={i} issue={issue} />)
      )}
    </div>
  )
}
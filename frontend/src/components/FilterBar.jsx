export default function FilterBar({ severity, setSeverity, hiddenAgents, setHiddenAgents, agents }) {
  function toggleAgent(name) {
    setHiddenAgents(prev =>
      prev.includes(name) ? prev.filter(a => a !== name) : [...prev, name]
    )
  }

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4 mt-6">
      <div className="flex flex-wrap items-center gap-6">
        <div>
          <p className="text-xs font-semibold text-gray-500 mb-2">SEVERITY</p>
          <div className="flex gap-2">
            {['all', 'critical', 'warning', 'info'].map(s => (
              <button
                key={s}
                onClick={() => setSeverity(s)}
                className={`text-xs px-3 py-1 rounded-full border transition capitalize ${
                  severity === s
                    ? 'bg-gray-800 text-white border-gray-800'
                    : 'border-gray-200 text-gray-600 hover:bg-gray-50'
                }`}
              >
                {s}
              </button>
            ))}
          </div>
        </div>

        <div>
          <p className="text-xs font-semibold text-gray-500 mb-2">AGENTS</p>
          <div className="flex gap-3 flex-wrap">
            {agents.map(agent => (
              <label key={agent.name} className="flex items-center gap-1.5 cursor-pointer">
                <input
                  type="checkbox"
                  checked={!hiddenAgents.includes(agent.name)}
                  onChange={() => toggleAgent(agent.name)}
                  className="rounded"
                />
                <span className="text-xs text-gray-600 capitalize">{agent.name}</span>
              </label>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
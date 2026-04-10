import CodeAnnotations from './components/CodeAnnotations'
import { useState } from 'react'
import CodeEditor, { SAMPLE_CODE } from './components/CodeEditor'
import SummaryPanel from './components/SummaryPanel'
import AgentCard from './components/AgentCard'
import FilterBar from './components/FilterBar'
import { useReview } from './hooks/useReview'
import './index.css'

export default function App() {
  const [code, setCode] = useState(SAMPLE_CODE)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [severity, setSeverity] = useState('all')
  const [hiddenAgents, setHiddenAgents] = useState([])
  const { submitReview } = useReview()

  async function handleSubmit() {
    setLoading(true)
    const data = await submitReview(code)
    setResult(data)
    setLoading(false)
  }

  function getFilteredAgents() {
    if (!result) return []
    return result.agents
      .filter(a => !hiddenAgents.includes(a.name))
      .map(a => ({
        ...a,
        issues: severity === 'all' ? a.issues : a.issues.filter(i => i.severity === severity)
      }))
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white border-b border-gray-200 px-6 py-4">
        <h1 className="text-xl font-semibold text-gray-800">MultiReview AI</h1>
        <p className="text-sm text-gray-500">Multi-agent code review system</p>
      </header>

      <main className="max-w-4xl mx-auto px-6 py-8">
        <CodeEditor
          code={code}
          onChange={setCode}
          onSubmit={handleSubmit}
          loading={loading}
        />
{loading && (
  <div className="mt-6 flex flex-col gap-4">
    {[1,2,3,4,5].map(i => (
      <div key={i} className="bg-white rounded-lg border border-gray-200 p-4 animate-pulse">
        <div className="flex items-center justify-between mb-3">
          <div className="flex gap-2">
            <div className="h-5 w-24 bg-gray-200 rounded" />
            <div className="h-5 w-16 bg-gray-100 rounded-full" />
          </div>
          <div className="h-4 w-20 bg-gray-100 rounded" />
        </div>
        <div className="h-4 w-full bg-gray-100 rounded mb-2" />
        <div className="h-4 w-3/4 bg-gray-100 rounded" />
      </div>
    ))}
  </div>
)}
        {result && (
          <>
            <SummaryPanel summary={result.summary} agents={result.agents} />
            <FilterBar
              severity={severity}
              setSeverity={setSeverity}
              hiddenAgents={hiddenAgents}
              setHiddenAgents={setHiddenAgents}
              agents={result.agents}
            />
            <div className="mt-6 flex flex-col gap-4">
              {getFilteredAgents().map(agent => (
                <AgentCard key={agent.name} agent={agent} />
              ))}
            </div>
            <CodeAnnotations code={code} agents={result.agents} />
          </>
        )}
      </main>
    </div>
  )
}
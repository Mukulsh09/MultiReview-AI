import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';

const SAMPLE_CODE = `def calculate(a, b):
    api_key = "sk-abc123hardcoded"
    x = 0
    for i in range(len(a)):
        for j in range(len(a)):
            x = x + a[i]
    result = a / b
    return result`;

export default function CodeEditor({ code, onChange, onSubmit, loading }) {
  return (
    <div className="bg-white rounded-lg border border-gray-200 overflow-hidden">
      <div className="bg-gray-50 px-4 py-2 border-b border-gray-200">
        <span className="text-sm font-medium text-gray-600">Python Code Editor</span>
      </div>

      <CodeMirror
        value={code}
        onChange={onChange}
        extensions={[python()]}
        minHeight="200px"
        theme="dark"
      />

      <div className="px-4 py-3 bg-gray-50 border-t border-gray-200 flex items-center justify-between">
        <span className="text-xs text-gray-400">
          {code.split('\n').length} lines · {code.length} characters
        </span>
        <button
          onClick={onSubmit}
          disabled={!code.trim() || loading}
          className="bg-blue-600 text-white px-5 py-2 rounded-md text-sm font-medium hover:bg-blue-700 disabled:opacity-40 disabled:cursor-not-allowed transition"
        >
          {loading ? 'Reviewing...' : 'Submit for Review'}
        </button>
      </div>
    </div>
  );
}

export { SAMPLE_CODE };
import { useState } from 'react'

export default function App() {
  const [word, setWord] = useState('')
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)

  async function handleSearch(e) {
    e.preventDefault()
    if (!word.trim()) return
    setLoading(true)
    try {
      const res = await fetch(`/api/search?word=${encodeURIComponent(word.trim())}`)
      const data = await res.json()
      setResults(data)
    } catch {
      setResults({ found: false, results: [] })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>Slownik Starszej Mowy</h1>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          value={word}
          onChange={(e) => setWord(e.target.value)}
          placeholder="Podaj polskie slowo..."
          autoFocus
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Szukam...' : 'Tlumacz'}
        </button>
      </form>

      {results !== null && (
        <div className="results">
          {results.found ? (
            <>
              <h2>W starszej mowie to znaczy:</h2>
              <p className="translation">{results.results.join(', ')}</p>
            </>
          ) : (
            <p className="not-found">Nie znaleziono tlumaczenia.</p>
          )}
          <button className="back" onClick={() => { setResults(null); setWord('') }}>
            Powrot
          </button>
        </div>
      )}
    </div>
  )
}

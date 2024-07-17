import React from 'react'
import './App.css'
import { fetchDate } from './apis/dates'

function App() {
  const [date, setDate] = React.useState()

  async function getDate() {
    await fetchDate().then((res: any) => {
      setDate(res.data.time)
    })
  }

  React.useEffect(() => {
    getDate()
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <div id="date-box">
          <h4>Date:</h4>
          <p>{date}</p>
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  )
}

export default App

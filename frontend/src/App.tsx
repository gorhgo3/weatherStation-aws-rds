import React from 'react'
import './App.css'
import { fetchDate } from './apis/dates'
import { fetchDevices } from './apis/devices'

interface DeviceType {
  id: number
  name: string
  device_type: string
  status: string
  last_updated: string
}

interface Devices {
  data: DeviceType[] | null
  selectedDevice: DeviceType | null
}

function App() {
  // handle later with TanStack wrapping
  const [date, setDate] = React.useState()
  const [devices, setDevices] = React.useState<Devices>({
    data: null,
    selectedDevice: null,
  })

  async function getDate() {
    await fetchDate().then((res: any) => {
      setDate(res.data.time)
    })
  }

  async function getDevices() {
    await fetchDevices().then((res) => {
      setDevices((prevState) => ({
        ...prevState,
        data: res.data.devices,
      }))
    })
  }

  React.useEffect(() => {
    getDate()
    getDevices()
  }, [])

  console.log(devices)

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
        <div id="devices-box">
          <h4>Devices:</h4>
          {devices.data && devices.data.map((device) => <p>{device.name}</p>)}
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

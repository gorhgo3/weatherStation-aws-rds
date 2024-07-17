import axios, { AxiosResponse } from 'axios'

interface DeviceType {
  id: number
  name: string
  device_type: string
  status: string
  last_updated: string
}

export async function fetchDevices(): Promise<
  AxiosResponse<any, DeviceType[]>
> {
  const url = 'http://127.0.0.1:8000/'
  return axios.get(url + 'getDevices/')
}

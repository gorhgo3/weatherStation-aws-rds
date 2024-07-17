import axios, { AxiosResponse } from 'axios'

export async function fetchDate(): Promise<AxiosResponse<any, any>> {
  const url = 'http://127.0.0.1:8000/'
  return axios.get(url + 'getTime/')
}

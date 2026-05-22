import API from './api'

export const registerUser = async (payload) => {
  const response = await API.post('/auth/signup', payload)
  return response.data
}

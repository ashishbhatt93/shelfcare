const handleSignup = async (e) => {
  e.preventDefault()

  try {
    const response = await registerUser({
      phone_number: phoneNumber,
      invite_code: inviteCode,
    })

    console.log(response)

    setMessage('Registration successful')

  } catch (err) {
    setMessage(
      err.response?.data?.detail || 'Signup failed'
    )
  }
}

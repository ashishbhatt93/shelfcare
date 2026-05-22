import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { useAuth } from '../../../hooks/useAuth'
import './Signup.css'

function Signup() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phoneNumber:'',
    inviteCode: '',
    password: '',
    confirmPassword: '',
  })
  const [errors, setErrors] = useState({})
  const [isSubmitting, setIsSubmitting] = useState(false)
  const { signup, error: authError } = useAuth()
  const navigate = useNavigate()

  const validateForm = () => {
    const newErrors = {}

    if (!formData.name.trim()) {
      newErrors.name = 'Name is required'
    } else if (formData.name.length < 2) {
      newErrors.name = 'Name must be at least 2 characters'
    }

    if (!formData.email.trim()) {
      newErrors.email = 'Email is required'
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email'
    }
    if (!formData.phoneNumber.trim()) {
      newErrors.phoneNumber = 'Phone number is required'
    } else if (!/^\d+$/.test(formData.phoneNumber)) {
      newErrors.phoneNumber = 'Phone number can only contain numbers'
    } else if (formData.phoneNumber.length !== 10){
      newErrors.phoneNumber = 'Phone number must be 10 digits'
    }
    if (!formData.inviteCode.trim()) {
      newErrors.inviteCode = 'Invite code is required'
    } else if (formData.inviteCode.trim().length < 1) {
      newErrors.inviteCode = 'Please enter a valid invite code'
    }

    if (!formData.password) {
      newErrors.password = 'Password is required'
    } else if (formData.password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters'
    }

    if (!formData.confirmPassword) {
      newErrors.confirmPassword = 'Please confirm your password'
    } else if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match'
    }

    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }))
    if (errors[name]) {
      setErrors((prev) => ({
        ...prev,
        [name]: '',
      }))
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!validateForm()) {
      return
    }

    setIsSubmitting(true)
    try {
  //    await signup(formData.email, formData.password, formData.name, formData.inviteCode)
      await signup({
        name: formData.name,
        email: formData.email,
        phone_number: formData.phoneNumber,
        password: formData.password,
        invite_code: formData.inviteCode,
      })
      alert('Account created successfully! Please login.')
      navigate('/dashboard')
    } catch (err) {
      console.error('Signup failed:', err)
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="signup-container">
      <div className="signup-box">
        <div className="signup-header">
          <h1>📚 Shelfcare</h1>
          <p>Join our reading community</p>
        </div>

        <form onSubmit={handleSubmit} className="signup-form">
          {authError && <div className="error-message">{authError}</div>}

          <div className="form-group">
            <label htmlFor="name">Full Name</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="John Doe"
              className={`form-input ${errors.name ? 'error' : ''}`}
            />
            {errors.name && <span className="error-text">{errors.name}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="email">Email Address</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="you@example.com"
              className={`form-input ${errors.email ? 'error' : ''}`}
            />
            {errors.email && <span className="error-text">{errors.email}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="phoneNumber">Phone Number</label>
            <input
              type="phoneNumber"
              id="phoneNumber"
              name="phonNumber"
              value={formData.phoneNumber}
              onChange={(e) => {
                const onlyNums = e.target.value.replace(/\D/g, '')
		setFormData((prev) => ({
		  ...prev,
		  phoneNumber: onlyNums,
		}))
	      }}
              placeholder="9876543210"
              className={`form-input ${errors.phoneNumber ? 'error' : ''}`}
            />
            {errors.phoneNumber && <span className="error-text">{errors.phoneNumber}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="inviteCode">Invite Code *</label>
            <input
              type="text"
              id="inviteCode"
              name="inviteCode"
              value={formData.inviteCode}
              onChange={handleChange}
              placeholder="Enter your invite code"
              className={`form-input ${errors.inviteCode ? 'error' : ''}`}
            />
            {errors.inviteCode && (
              <span className="error-text">{errors.inviteCode}</span>
            )}
            <p className="hint-text">You need an invite code to create an account</p>
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="At least 6 characters"
              className={`form-input ${errors.password ? 'error' : ''}`}
            />
            {errors.password && (
              <span className="error-text">{errors.password}</span>
            )}
          </div>

          <div className="form-group">
            <label htmlFor="confirmPassword">Confirm Password</label>
            <input
              type="password"
              id="confirmPassword"
              name="confirmPassword"
              value={formData.confirmPassword}
              onChange={handleChange}
              placeholder="Confirm your password"
              className={`form-input ${errors.confirmPassword ? 'error' : ''}`}
            />
            {errors.confirmPassword && (
              <span className="error-text">{errors.confirmPassword}</span>
            )}
          </div>

          <button
            type="submit"
            disabled={isSubmitting}
            className="signup-button"
          >
            {isSubmitting ? 'Creating account...' : 'Create Account'}
          </button>
        </form>

        <div className="signup-footer">
          <p>
            Already have an account?{' '}
            <Link to="/login" className="login-link">
              Sign in here
            </Link>
          </p>
        </div>
      </div>
    </div>
  )
}

export default Signup

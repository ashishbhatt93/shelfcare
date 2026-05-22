function FeatureCard({ icon, title, description }) {
  return (
    <div className="card" style={{ textAlign: 'center', padding: '2.5rem' }}>
      <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>
        {icon}
      </div>
      <h3 className="mb-2">{title}</h3>
      <p className="text-muted">{description}</p>
    </div>
  )
}

export default FeatureCard

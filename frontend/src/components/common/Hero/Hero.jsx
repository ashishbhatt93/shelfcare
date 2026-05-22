function Hero({ title, subtitle, cta, image }) {
  return (
    <div className="section section-hero container-sm">
      <div className="fade-in">
        <h1 className="mb-4">{title}</h1>
        <p className="text-secondary mb-5" style={{ fontSize: '1.3rem' }}>
          {subtitle}
        </p>
        {cta && (
          <div className="flex flex-center" style={{ gap: '1rem', justifyContent: 'center' }}>
            <button className="btn btn-primary" style={{ fontSize: '1.1rem', padding: '0.9rem 2rem' }}>
              {cta.primary}
            </button>
            <button className="btn btn-secondary" style={{ fontSize: '1.1rem', padding: '0.9rem 2rem' }}>
              {cta.secondary}
            </button>
          </div>
        )}
        {image && (
          <div className="mt-5">
            <img 
              src={image} 
              alt="Hero" 
              style={{ 
                width: '100%', 
                maxWidth: '600px',
                borderRadius: '12px',
                marginTop: '2rem'
              }} 
            />
          </div>
        )}
      </div>
    </div>
  )
}

export default Hero

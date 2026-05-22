import Hero from '../components/common/Hero/Hero'
import FeatureCard from '../components/common/FeatureCard/FeatureCard'
import Section from '../components/common/Section/Section'
import { useAuth } from '../hooks/useAuth'

function Home() {
  const { user } = useAuth()

  return (
    <div>
      {/* Hero Section */}
      <Hero
        title="Your Personal Library"
        subtitle="Discover, track, and organize your reading journey. From discovery to completion, manage your books effortlessly."
        cta={{
          primary: 'Start Reading',
          secondary: 'Explore Books',
        }}
      />

      {/* Features Section */}
      <Section alt>
        <div className="container-sm">
          <h2 style={{ textAlign: 'center', marginBottom: '3rem' }}>
            Everything you need to manage your books
          </h2>
          <div className="grid grid-3">
            <FeatureCard
              icon="📚"
              title="Smart Library"
              description="Organize and manage all your books in one beautiful, intuitive interface."
            />
            <FeatureCard
              icon="📱"
              title="Quick Add"
              description="Scan book covers with OCR or add books manually with just a few taps."
            />
            <FeatureCard
              icon="⭐"
              title="Watchlist"
              description="Keep track of books you want to read and get personalized recommendations."
            />
          </div>
        </div>
      </Section>

      {/* CTA Section */}
      <Section>
        <div className="container-sm text-center">
          <h2 className="mb-4">Ready to start?</h2>
          <p style={{ marginBottom: '2rem', fontSize: '1.1rem' }}>
            Join thousands of readers building their perfect library.
          </p>
          <button className="btn btn-primary" style={{ fontSize: '1.1rem', padding: '0.9rem 2rem' }}>
            Explore Your Books
          </button>
        </div>
      </Section>
    </div>
  )
}

export default Home

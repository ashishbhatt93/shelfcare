function Section({ children, alt, id }) {
  return (
    <section 
      id={id}
      className={`section ${alt ? 'section-alt' : ''}`}
    >
      {children}
    </section>
  )
}

export default Section

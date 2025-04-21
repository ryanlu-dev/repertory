<script>
  // Home page component
</script>

<svelte:head>
  <title>Repertory - Track Your Musical Journey</title>
</svelte:head>

<section class="hero">
  <h1>Track Your Musical Journey</h1>
  <p>A platform for musicians to log performances, build repertoire, and earn achievements</p>
  <div class="cta-buttons">
    <button class="primary">Sign Up</button>
    <button class="secondary">Learn More</button>
  </div>
</section>

<section class="features">
  <div class="feature">
    <h2>Performance Tracking</h2>
    <p>Log your performances including venue, ensemble, and pieces played</p>
  </div>
  <div class="feature">
    <h2>Repertoire Building</h2>
    <p>Build and showcase your musical repertoire</p>
  </div>
  <div class="feature">
    <h2>Achievement System</h2>
    <p>Earn achievements for your musical accomplishments</p>
  </div>
</section>

<style>
  .hero {
    text-align: center;
    padding: 4rem 1rem;
    background-color: #f1faee;
    border-radius: 8px;
    margin-bottom: 2rem;
  }

  .hero h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #1d3557;
  }

  .cta-buttons {
    margin-top: 2rem;
  }

  button {
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    font-weight: bold;
    margin: 0 0.5rem;
    cursor: pointer;
  }

  button.primary {
    background-color: #e63946;
    color: white;
    border: none;
  }

  button.secondary {
    background-color: transparent;
    color: #1d3557;
    border: 2px solid #1d3557;
  }

  .features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }

  .feature {
    background-color: #a8dadc;
    padding: 2rem;
    border-radius: 8px;
    text-align: center;
  }

  .feature h2 {
    color: #1d3557;
    margin-bottom: 1rem;
  }
</style>
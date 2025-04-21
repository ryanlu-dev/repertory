<script lang="ts">
	import '../app.css';

	let { children } = $props();
</script>

<div class="app">
  <header>
    <div class="header-content">
      <h1>Repertory</h1>
      <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
      </nav>
    </div>
  </header>

  <main>
    {@render children()}
  </main>

  <footer>
    <p>&copy; 2025 Repertory</p>
  </footer>
</div>

<style>
  .app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  header {
    background-color: #1d3557;
    color: white;
    padding: 1rem;
  }

  .header-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  h1 {
    margin: 0;
  }

  nav a {
    color: white;
    margin-left: 1rem;
    text-decoration: none;
  }

  nav a:hover {
    text-decoration: underline;
  }

  main {
    flex: 1;
    padding: 1rem;
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
  }

  footer {
    background-color: #f1faee;
    padding: 1rem;
    text-align: center;
  }
</style>
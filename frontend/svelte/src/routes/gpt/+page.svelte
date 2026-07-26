<script lang='ts'>
  const resources = {
    metal: 523421,
    crystal: 182340,
    deuterium: 85420,
    energy: 9450,
    darkMatter: 1275
  };

  const planets = [
    {
      name: "Earth",
      coords: "[1:234:8]",
      temperature: "-12°C to 28°C",
      fields: "152 / 188"
    }
  ];

  const fleets = [
    {
      mission: "Transport",
      destination: "[1:233:12]",
      remaining: "00:12:43"
    },
    {
      mission: "Expedition",
      destination: "[16:999:7]",
      remaining: "01:43:10"
    }
  ];

  const shortcuts = [
    "Buildings",
    "Research",
    "Shipyard",
    "Defense",
    "Galaxy",
    "Fleet",
    "Alliance"
  ];

  import { onMount } from "svelte";

  let player = $state();

  

  onMount(async () => {
    try {
      const res = await fetch("http://localhost:5000/status", {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'player': '1'
        }
      });
      player = await res.json();
    } catch ( err ) {
      console.error(err);
    }
  });

</script>

<svelte:head>
  <title>Galatic Expansions</title>
</svelte:head>

<div class="app">

  <!-- Top Bar -->

  <header class="topbar">

    <div class="logo">
      Galatic Expansions
    </div>

    <div class="resources">

      <div class="resource metal">
        <span>Metal</span>
        <strong>{player?.metal.toLocaleString()}</strong>
      </div>

      <div class="resource crystal">
        <span>Crystal</span>
        <strong>{player?.crystal.toLocaleString()}</strong>
      </div>

      <div class="resource deut">
        <span>Deuterium</span>
        <strong>{resources.deuterium.toLocaleString()}</strong>
      </div>

      <div class="resource energy">
        <span>Energy</span>
        <strong>{resources.energy.toLocaleString()}</strong>
      </div>

      <div class="resource dm">
        <span>Dark Matter</span>
        <strong>{resources.darkMatter.toLocaleString()}</strong>
      </div>

    </div>

  </header>

  <div class="layout">

    <!-- Sidebar -->

    <aside class="sidebar">

      <h3>Navigation</h3>

      {#each shortcuts as item}
        <button>{item}</button>
      {/each}

    </aside>

    <!-- Main -->

    <main>

      <section class="hero card">

        <div>

          <h1>{planets[0].name}</h1>

          <p>{planets[0].coords}</p>

          <p>{planets[0].temperature}</p>

          <p>Fields: {planets[0].fields}</p>

        </div>

        <div class="planet"></div>

      </section>

      <section class="grid">

        <div class="card">

          <h2>Fleet Movement</h2>

          {#each fleets as fleet}

            <div class="fleet">

              <div>
                <strong>{fleet.mission}</strong>
              </div>

              <div>{fleet.destination}</div>

              <div>{fleet.remaining}</div>

            </div>

          {/each}

        </div>

        <div class="card">

          <h2>Empire</h2>

          <ul>

            <li>Points: 2,104,522</li>

            <li>Rank: #42</li>

            <li>Colonies: 8</li>

            <li>Research: 78%</li>

            <li>Fleet Power: Strong</li>

          </ul>

        </div>

      </section>

      <section class="card">

        <h2>Construction Queue</h2>

        <div class="queue">

          <div class="item">
            <span>Metal Mine 29 → 30</span>
            <span>3h 24m</span>
          </div>

          <div class="item">
            <span>Research Lab 15 → 16</span>
            <span>7h 11m</span>
          </div>

        </div>

      </section>

      <section class="card">

        <h2>Commander Messages</h2>

        <div class="message">

          ✔ Expedition returned successfully.

        </div>

        <div class="message">

          ⚠ Fleet detected near colony.

        </div>

      </section>

    </main>

  </div>

</div>

<style>

:global(body) {
  margin:0;
  font-family:Inter,Segoe UI,sans-serif;
  background:#070b13;
  color:white;
}

.app{
  min-height:100vh;
  background:
    radial-gradient(circle at top,#203454,#070b13 60%);
}

.topbar{

  display:flex;
  justify-content:space-between;
  align-items:center;

  padding:18px 30px;

  border-bottom:1px solid rgba(255,255,255,.08);

  backdrop-filter:blur(10px);

}

.logo{
  font-size:24px;
  font-weight:700;
  letter-spacing:2px;
}

.resources{

  display:flex;
  gap:16px;

}

.resource{

  background:#111a2a;
  padding:10px 16px;
  border-radius:8px;
  text-align:center;
  min-width:110px;

}

.resource span{

  display:block;
  font-size:12px;
  opacity:.7;

}

.resource strong{

  color:#82d8ff;
  font-size:18px;

}

.layout{

  display:grid;
  grid-template-columns:220px 1fr;

}

.sidebar{

  padding:24px;
  border-right:1px solid rgba(255,255,255,.08);

}

.sidebar h3{

  color:#8fcfff;

}

.sidebar button{

  width:100%;
  margin-top:12px;

  background:#152238;

  color:white;

  border:none;

  padding:12px;

  border-radius:8px;

  cursor:pointer;

  transition:.2s;

}

.sidebar button:hover{

  background:#24406d;

}

main{

  padding:28px;

}

.hero{

  display:flex;
  justify-content:space-between;
  align-items:center;

}

.planet{

  width:220px;
  height:220px;

  border-radius:50%;

  background:
    radial-gradient(circle at 35% 35%,#6ec8ff,#264577,#081420);

  box-shadow:
      0 0 40px rgba(60,160,255,.4);

}

.grid{

  display:grid;

  grid-template-columns:1fr 1fr;

  gap:20px;

  margin-top:20px;

}

.card{

  background:rgba(18,25,40,.9);

  border:1px solid rgba(255,255,255,.08);

  border-radius:14px;

  padding:22px;

  margin-bottom:20px;

}

.fleet{

  display:grid;

  grid-template-columns:1fr auto auto;

  padding:12px 0;

  border-bottom:1px solid rgba(255,255,255,.08);

}

.queue .item{

  display:flex;

  justify-content:space-between;

  padding:14px 0;

  border-bottom:1px solid rgba(255,255,255,.08);

}

.message{

  background:#12263f;

  padding:14px;

  margin-top:12px;

  border-radius:8px;

}

@media(max-width:900px){

.layout{
  grid-template-columns:1fr;
}

.sidebar{
  border-right:none;
  border-bottom:1px solid rgba(255,255,255,.08);
}

.resources{
  flex-wrap:wrap;
}

.grid{
  grid-template-columns:1fr;
}

.hero{
  flex-direction:column;
  gap:24px;
}

}

</style>
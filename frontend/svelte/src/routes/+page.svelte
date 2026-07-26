<script lang="ts">
    let data = $state();

    async function roll() {
        console.log("roll clicked");
		const response = await fetch('http://localhost:5000/dump');
		data = await response.json();
	}
</script>

<button onclick={roll}>Roll the dice</button>

{#if data !== undefined}
	<p>we got {data}</p>
{/if}

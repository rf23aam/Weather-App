
<script>
	let city = 'London';
	let temperature = null;
	let condition = null;
	let error = null;
	let backendport = 'http://localhost:5000';
  
	async function fetchWeather() {
	  const response = await fetch(`${backendport}/weather/${city}`);
	  const data = await response.json();
	  if(data.error !== null)
	  {
		error = data.error;
	  }	  
	  temperature = data.temperature;
	  condition = data.condition;
	}
 
  </script>

  <h1>Current Weather</h1>
  <form on:submit|preventDefault={fetchWeather}>
	<label for="city">City:</label>

    <select bind:value={city}>
        <option value="London">London</option>
        <option value="New York">New York</option>
        <option value="Paris">Paris</option>
    </select>
	<button type="submit">Get Weather</button>

</form>

  
  {#if temperature !== null && condition !== null && temperature !== 'undefined'}
	<p>Temperature: {temperature}°C</p>
	<p>Condition: {condition}</p>
  {:else if error !== null}
	<p>{error}</p>
  {:else}
  <p>No data available..</p>
  {/if}
  
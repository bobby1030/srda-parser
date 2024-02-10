export async function load({ fetch, params }) {

	let data = await fetch('/api/codebooks/');
	let codebooks = await data.json()

	return {
		codebooks
	}
}
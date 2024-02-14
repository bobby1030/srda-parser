export async function load({ fetch, params }) {
    const codebook_id = params.slug;

    const codebook = await fetch(`/api/codebooks/${codebook_id}`).then(res => res.json());

    return {
        codebook
    };
}

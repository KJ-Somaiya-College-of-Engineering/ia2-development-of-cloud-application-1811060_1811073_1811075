import baseUrl from "./baseUrl"

export default async function(context, title, description, image, durl, urlid) {
    const token = context.$store.state.authToken;
    context.$axios.setHeader('token', token);
    context.$axios.setHeader('Content-Type', 'application/json')
    const response = await context.$axios.$post(
        `${baseUrl}/url/update/ogdata?urlid=${urlid}`,
        {
        title,
        description,
        image,
        durl
    });
    if(response.STATUS == "OK") return [true, undefined];
    else if(response.STATUS == "FAIL") return [false, "Server Error"];
    return [false, "Contact Developers"]
}
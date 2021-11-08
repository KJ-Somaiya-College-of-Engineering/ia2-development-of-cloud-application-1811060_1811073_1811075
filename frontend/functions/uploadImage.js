import baseUrl from "@/functions/baseUrl"

export default async function (context, fileRef) {
    if(!fileRef) return [false, "Image not selected."]
    const token = context.$store.getters.getAuthToken;
    if(!token)return [false, "Auth Error. Refresh this page."]
    const form = new FormData();
    form.append("cover", fileRef, fileRef.name);
    context.$axios.setHeader("token", token);
    context.$axios.setHeader("Content-Type", "multipart/form-data")
    var response;
    try {
        response = await context.$axios.$post(
        `${baseUrl}/image/upload`,
        form
    )
    } catch(error) {
        console.error(error)
    }
    if(response.STATUS == "OK") return [true, response.IMAGE_URL];
    else if(response.STATUS == "FAIL") return [false, response.MSG];
    return [false, "Contact Developers"]
}
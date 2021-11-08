<template>
  <div class="card">
      <div class="card-content">
          <div class="content trbg">
                <div class="title is-2">
                    🎉 URL Shortened Successfully!
                </div>
                <div class="subtitle">
                    You can now do further customisations by clicking <strong>"Customise"</strong> button.
                </div>
                <hr>
                <div class="columns">
                    <div class="column is-3">
                        <img :src="imagelink" alt="Image Link">
                    </div>
                    <div class="column is-8">
                        <div class="title">
                            {{ title }}
                        </div>
                        <div class="subtitle">
                            {{ subtitle }}
                        </div>
                    </div>
                </div>
                <div class="field">
                    <div class="control has-icons-right columns">
                        <input class="input is-large column is-8" type="text" v-model="link" style="border: 2px solid #67d3b3; color: #56ae94;" disabled/>
                        <button class="button is-large is-primary column is-4" v-on:click.prevent="copythis()">
                            Copy
                        </button>
                    </div>
                </div>
                <hr>
          </div>
      </div>
  </div>
</template>

<script>
export default {
    props: {
        urlObj: {
            required: true,
            type: Object
        }
    },
    data(){
        return {
            link: "https://trcr.tk/" + this.urlObj._id,
            title: this.urlObj?.url_og.title,
            subtitle: this.urlObj?.url_og.description,
            imagelink: this.urlObj?.url_og.image
        }
    },
    methods: {
        copythis(){
            this.$clipboard(this.link);
            this.$toasted.success("URL Copied Successfully.", {
                theme: "outline",
                position: "top-right",
                duration: 3000
            })
        }
    }
}
</script>

<style>
.trbg {
    background-image: url("../assets/images/trcrbg.png");
}
</style>
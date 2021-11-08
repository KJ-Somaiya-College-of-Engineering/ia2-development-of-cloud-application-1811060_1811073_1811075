<template>
  <div class="card">
      <div class="card-header">
          <div class="card-header-title">
              <div class="title is-5">
                  Customise URL
                  <span class="tag is-danger">Beta</span>
              </div>
          </div>
          <div class="card-header-icon">
              <span class="icon is-small">
                <i class="fas fa-edit"></i>
            </span>
          </div>
      </div>
      <div class="card-content">
          <div class="content">
              <div class="columns">
                  <div class="column is-6">
                      <div class="card previewcard">
                          <div class="card-content">
                              <center><div class="title is-4">Preview</div></center>
                                <hr style="margin: 10px; margin-bottom: 20px;">
                                    <div class="wacontainer">
                                        <img class="prevtemplate" src="~/assets/images/wa_ios_template.jpg"/>
                                        <div class="prevtitledesc">
                                            <b><p class="prevtitle">{{ applyShortening(title, 36) }}</p></b>
                                            <p class="prevdesc">{{ applyShortening(description, 72) }}</p>
                                        </div>
                                        <div class="previmage"><img :src="coverURL" style="border-radius: 5%;"></div>
                                        <div class="prevurl"><p class="prevurltext">{{ url }}</p></div>
                                    </div>
                          </div>
                      </div>
                  </div>
                  <div class="column is-6">
                      <form>
                            <div class="field">
                                <div class="control has-icons-left has-icons-right">
                                <input class="input" type="text" placeholder="Title" v-model="title" />
                                <span class="icon is-small is-left">
                                    <i class="fas fa-heading"></i>
                                </span>
                                </div>
                            </div>
                            <div class="field">
                                <div class="control has-icons-left has-icons-right">
                                <input class="input" type="email" placeholder="Description" v-model="description"/>
                                <span class="icon is-small is-left">
                                    <i class="fas fa-file-alt"></i>
                                </span>
                                </div>
                            </div>
                            <div class="field">
                                <div class="file has-name">
                                    <label class="file-label">
                                        <input class="file-input" type="file" @change="imageSelected">
                                        <span class="file-cta">
                                        <span class="file-icon">
                                            <i class="fas fa-upload"></i>
                                        </span>
                                        <span class="file-label">
                                            Choose Image
                                        </span>
                                        </span>
                                        <span class="file-name">
                                            <p v-if="isImageSelected">
                                                Image Selected!
                                            </p>
                                            <p v-else>
                                                Image for Preview
                                            </p>
                                        </span>
                                    </label>
                                </div>
                            </div>
                            <button class="button is-fullwidth is-primary is-loading" v-if="isCustomiseLoading"></button>
                            <button class="button is-fullwidth is-primary" v-on:click.prevent="initiateCustomise()" v-else>
                                <span class="icon is-small">
                                    <i class="fas fa-magic"></i>
                                </span>&nbsp;&nbsp;&nbsp;
                                Customise
                            </button>
                        </form>
                  </div>
                  <div v-if="showCropper">
                    <transition name="modal">
                        <div class="modal-mask">
                        <div class="modal-wrapper">
                            <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                <h4 class="modal-title">Adjust Your Cover</h4>
                                </div>
                                <div class="modal-body">
                                <div class="card">
                                    <div class="card-content">
                                    <img
                                        ref="imgCover"
                                        :src="coverURL"
                                        height="350px"
                                        style="max-width: 100%"
                                    />
                                    <div class="d-grid gap-2 d-md-block">
                                        <button class="button" v-on:click.prevent="updateCanvas()">Done</button>
                                        <button
                                        class="button"
                                        v-on:click.prevent="cancelUpload()"
                                        >Cancel</button>
                                    </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </transition>
                    </div>

              </div>
          </div>
      </div>
  </div>
</template>

<script>
import Cropper from "cropperjs";
import uploadImage from "@/functions/uploadImage"
import updateOgData from "@/functions/updateOgData"

export default {
    props: {
        urlObj: {
            type: Object,
            required: true
        },
        closeCustomiseCard: {
            required: true
        }
    },
    data(){
        return {
            title: this.urlObj.title,
            description: this.urlObj.url_og?.description,
            url: this.urlObj.url_og?.url,
            selectedImage: null,
            coverURL: this.urlObj.url_og?.image,
            isImageSelected: false,
            showCropper: false,
            cropper: {},
            finalblob: {},
            isCustomiseLoading: false
        }
    },
    methods: {
        applyShortening(string, len) {
            if (string?.length > len) {
                const str1 = string.substr(0, len-3);
                const str2 = "...";
                return str1 + str2;
            }
            return string;
        },
        imageSelected(event){
            this.selectedImage = event.target.files[0];
            if(!this.selectedImage) return;
            this.isImageSelected = true;
            this.coverURL = URL.createObjectURL(this.selectedImage);
            this.showCropper = true;
            this.$nextTick(() => {
                this.cropper = new Cropper(this.$refs.imgCover, {
                    zoomable: false,
                    scalable: false,
                    aspectRatio: 1,
                });
            });
        },
        cancelUpload() {
            this.selectedImage = null;
            this.isImageSelected = false;
            this.coverURL = null
            this.showCropper = false;
        },
        updateCanvas() {
            this.showCropper = false;
            this.coverURL = this.cropper.getCroppedCanvas().toDataURL();
        },
        async requestUpdate(title, description, imageUrl, durl, urlid) {
            const result = await updateOgData(this, title, description, imageUrl, durl, urlid);
            if(result[0]){
                this.closeCustomiseCard(true, "URL Updated Successfully.\nYou will now be able to see changes while sharing.")
            } else {
                this.closeCustomiseCard(false, result[1])
            }
        },
        async initiateCustomise() {
            this.isCustomiseLoading = true;
            let imageUrl = undefined;
            if(this.selectedImage) {
                    this.cropper.getCroppedCanvas().toBlob(async (blob) => {
                    const farray = blob.type.split("/");
                    const filename = "banner." + farray[farray.length - 1];
                    blob.name = filename;
                    this.finalblob = blob;
                    const result = await uploadImage(this, this.finalblob);
                    if(result[0]){
                        imageUrl = result[1]
                        await this.requestUpdate(this.title, this.description, imageUrl, this.url, this.urlObj._id);
                    }
                    else{
                        this.closeCustomiseCard(false, result[1]);
                        return;
                    }
                    this.urlObj.url_og.image = imageUrl
                });
            }
            else {
                imageUrl = this.coverURL;
                await this.requestUpdate(this.title, this.description, imageUrl, this.url, this.urlObj._id);
            }
            this.urlObj.title = this.title;
            this.urlObj.url_og.description = this.description;
            this.urlObj.url_og.title = this.title;
            this.isCustomiseLoading = false;
        }
    }
}
</script>

<style>
.prevtemplate {
    position: absolute;
    border: 0.2px solid #cfcfcf;
}

.prevtitledesc {
    position: absolute;
    left: 82px;
    top: 6px;
    width: 180px;
    line-height: 12px;
}

.prevtitle {
    font-size: 12px;
}

.prevdesc {
    font-size: 12px;
    color: #6f6f6f;
}

.previmage {
    position: absolute;
    left: 6px;
    top: 5px;
    width: 70px;
    height: 10px;
}

.prevurl {
    position: absolute;
    left: 82px;
    top: 68px;
    width: 180px;
    line-height: 12px;
}

.prevurltext {
    font-size: 12px;
    color: gray;
}

.prevmsg {
    position: absolute;
    left: 48px;
    top: 95px;
    width: 180px;
    line-height: 12px;
}

.prevmsgtext {
    font-size: 14px;
}

.wacontainer {
    position: relative;
}

.previewcard {
    height: 250px;
}

@media (max-width: 319px){
    .prevtitledesc {
        left: 49px;
        width: 120px;
    }
    .previmage {
        height: 8px;
        width: 34px;
    }
    .prevtitle {
        font-size: 8px;
    }
    .prevdesc {
        font-size: 8px;
        color: #6f6f6f;
    }
    .prevurl {
        top: 44px;
        left: 49px;
    }
    .prevurltext {
        font-size: 8px;
    }
}


@media (max-width: 360px) and (min-width: 320px){
    .prevtitledesc {
        left: 65px;
        width: 120px;
    }
    .previmage {
        height: 7px;
        width: 50px;
    }
    .prevtitle {
        font-size: 10px;
    }
    .prevdesc {
        font-size: 10px;
        color: #6f6f6f;
    }
    .prevurl {
        top: 54px;
        left: 65px;
    }
    .prevurltext {
        font-size: 10px;
    }
};

@media (max-width: 390px) and (min-width: 361px){
    .prevtitledesc {
        left: 70px;
        width: 170px;
    }
    .previmage {
        height: 10px;
        width: 55px;
    }
    .prevtitle {
        font-size: 11px;
    }
    .prevdesc {
        font-size: 11px;
        color: #6f6f6f;
    }
    .prevurl {
        top: 68px;
        left: 70px;
    }
    .prevurltext {
        font-size: 11px;
    }
};

@media (max-width: 430px) and (min-width: 391px){
    .prevtitledesc {
        left: 75px;
        width: 190px;
        line-height: 13px;
    }
    .previmage {
        height: 12px;
        width: 60px;
    }
    .prevtitle {
        font-size: 12px;
    }
    .prevdesc {
        font-size: 12px;
        color: #6f6f6f;
    }
    .prevurl {
        top: 72px;
        left: 75px;
    }
    .prevurltext {
        font-size: 12px;
    }
};

@media (max-width: 491px) and (min-width: 431px) {
    .prevtitledesc {
        left: 85px;
        width: 190px;
    }
    .previmage {
        height: 15px;
        width: 70px;
    }
    .prevtitle {
        font-size: 12px;
    }
    .prevdesc {
        font-size: 12px;
        color: #6f6f6f;
    }
    .prevurl {
        top: 90px;
        left: 85px;
    }
    .prevurltext {
        font-size: 12px;
    }
}

@media (max-width: 650px) and (min-width: 492px){
    .prevtitledesc {
        left: 94px;
        width: 190px;
        line-height: 16px;
    }
    .previmage {
        height: 25px;
        width: 80px;
    }
    .prevtitle {
        font-size: 14px;
    }
    .prevdesc {
        font-size: 14px;
        color: #6f6f6f;
    }
    .prevurl {
        top: 110px;
        left: 94px;
    }
    .prevurltext {
        font-size: 14px;
    }
    .previewcard {
        height: 350px;
    }
}

@media (max-width: 760px) and (min-width: 651px) {
    .prevtitledesc {
        left: 144px;
        width: 320px;
        line-height: 21px;
    }
    .previmage {
        height: 40px;
        width: 130px;
    }
    .prevtitle {
        font-size: 18px;
    }
    .prevdesc {
        font-size: 18px;
        color: #6f6f6f;
    }
    .prevurl {
        top: 150px;
        left: 144px;
    }
    .prevurltext {
        font-size: 18px;
    }
    .previewcard {
        height: 400px;
    }
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 80vh;
  height: 80vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}
.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.cropperimg{
  max-width: 100%;
}
</style>
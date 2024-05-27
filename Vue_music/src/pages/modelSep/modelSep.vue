<template>
  <div class="comment">
    <div class="main-box">
      <div id="wavesurfer"></div>
    </div>
    <span>音频原声</span>
    <div class="main-button">
      <button class="button" @click="start()">播放</button>
      <button class="button" @click="end()">暂停</button>
      <button class="button" @click="getSepTwo()">两音轨</button>
    </div>
    <div v-show="hide1">
      <div class="main-box">
        <div id="waveform1"></div>
      </div>
      <span>人声部分</span>
      <div class="main-button">
        <button class="button" @click="getMusic0_p()">play</button>
        <button class="button" @click="getMusic0_e()">pause</button>
      </div>
      <div class="main-box">
        <div id="waveform2"></div>
      </div>
      <span>乐器部分</span>
      <div class="main-button">
        <button class="button" @click="getMusic1_p()">play</button>
        <button class="button" @click="getMusic1_e()">pause</button>
      </div>
    </div>
  </div>
</template>

<script>
import { loadMixin } from '@/utils/mixin'
import WaveSurfer from 'wavesurfer.js'
import { getMusicSep, getMusicUrl, searchHot } from '@/api/index.js'
import axios from 'axios'

function getWaveS(name) {
  const Wave = WaveSurfer.create({
    container: '#' + name,
    height: 150,
    progressColor: '#a3abab',
    waveColor: '#88d562',
    cursorColor: '#FFDDDD',
    barWidth: 1,
    mediaControls: false,
    backend: 'MediaElement',
  })
  return Wave
}
export default {
  mixins: [loadMixin],
  data() {
    return {
      hide1: false,
      musicUrl: '',
      wavesurfer: null,
      musicData: null,
      wave1: null,
      wave2: null,
    }
  },
  created() {
    {
      this.init()
    }
  },
  methods: {
    // 初始化
    init() {
      getMusicUrl(this.$route.params.id).then((res) => {
        console.log(this.musicUrl)
        this.musicUrl = res.data[0].url
        console.log('获得该音乐链接:', this.musicUrl)
        this.wavesurfer = getWaveS('wavesurfer')
        this.wavesurfer.load(this.musicUrl)
        // 下载到本地
        axios({
          url: this.musicUrl,
          method: 'GET',
          responseType: 'blob',
        }).then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]))
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', 'music.mp3')
          document.body.appendChild(link)
          link.click()
        })
      })
    },
    getSepTwo() {
      try {
        const response = axios.get('http://localhost:5000/api/model')
        this.message = response.data.message
        console.log(this.message)
      } catch (error) {
        console.log(error)
      }
      // this.get_data()
    },
    async get_data() {
      // const objectURL = URL.createObjectURL(this.musicData)
      // this.wave1.load(objectURL)
      // this.hide1 = !this.hide1
    },
    // async fetchAudioFile(fileUrl) {
    //   return new Promise((resolve, reject) => {
    //     setTimeout(() => {
    //       const audioFile = fileUrl
    //       resolve(audioFile)
    //     }, 2000)
    //   })
    // },
    start() {
      this.wavesurfer.play(0)
    },
    end() {
      this.wavesurfer.pause()
    },
    getMusic0_p() {
      this.wave1.play(0)
    },
    getMusic0_e() {
      this.wave1.pause()
    },
    getMusic1_p() {
      // console.info(this.Sep_wave[1])
      this.wave2.play(0)
    },
    getMusic1_e() {
      // console.info(this.Sep_wave[1])
      this.wave2.pause()
    },
  },
}
</script>

<style lang="less" scoped>
.button {
  background-color: #2e6462;
  margin-left: 10px;
  margin-top: 10px;
  color: white;
  width: 100px;
  height: 30px;
  border: 0;
  font-size: 16px;
  border-radius: 30px;
}

.comment {
  .comment-list {
    padding: 0 10px;
  }

  .comment-title {
    position: sticky;
    top: 0;
    z-index: 1;
    margin: 0 -10px;
    padding: 10px;
    height: 34px;
    line-height: 34px;
    color: @text_color_active;
    background: @header_bg_color;
    backdrop-filter: @backdrop_filter;
  }
  .comment-item {
    position: relative;
    padding: 15px 0 15px 55px;
    & + .comment-item {
      border-top: 1px solid @comment_item_line_color;
    }
    &-pic {
      display: block;
      position: absolute;
      left: 0;
      top: 20px;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      overflow: hidden;
    }
    &-title {
      height: 20px;
      margin-bottom: 6px;
      font-weight: 400;
      .no-wrap();
      color: @text_color_active;
    }
    &-disc {
      overflow: hidden;
      word-break: break-all;
      word-wrap: break-word;
      line-height: 25px;
      text-align: justify;
      color: @text_color;
      img {
        position: relative;
        vertical-align: middle;
        top: -2px;
      }
    }
    &-replied {
      padding: 8px 19px;
      margin-top: 10px;
      line-height: 20px;
      border: 1px solid @comment_replied_line_color;
      a {
        color: @text_color_active;
      }
    }
    &-opt {
      margin-top: 10px;
      line-height: 25px;
      text-align: right;
      overflow: hidden;
      .comment-opt-date {
        float: left;
        line-height: 28px;
      }
      .comment-opt-liked {
        display: inline-block;
        height: 20px;
        line-height: 20px;
      }
    }
  }
}
</style>

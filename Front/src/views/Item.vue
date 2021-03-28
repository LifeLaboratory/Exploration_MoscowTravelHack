<template>
  <div>
    <header style="height: 80px; background-color: white; box-shadow: 0 2px 3px 1px rgba(0, 0, 0, .2);">
      <a href="/"><img src="../assets/logo_life.png" style="float: left; height: 80px" /></a>
      <a-menu mode="horizontal" style="height: 80px; float: left; margin-left: 50px;">
        <a-menu-item class="header__nav-link">Города и районы</a-menu-item>
        <a-menu-item class="header__nav-link">Путеводитель</a-menu-item>
        <a-menu-item class="header__nav-link">Экскурсии</a-menu-item>
        <a-menu-item class="header__nav-link">Афиша</a-menu-item>
        <a-menu-item class="header__nav-link">Блог</a-menu-item>
        <a-menu-item class="header__nav-link">Карта</a-menu-item>
      </a-menu>
    </header>
    <a-row type="flex" style="padding-top: 80px;">
      <a-col :span="22" style="margin: 0 auto;">
        <a-row>
          <h1 style="font-size: 42px; float: left; font-weight: bold; margin-top: 40px;">{{this.item.title}}</h1>
        </a-row>
        <a-row style="background-color: #e6e9eb; padding: 36px; margin-top: 24px;">
          <img slot="cover" alt="example" :src="this.item.images"/>
          <img :src="this.item.images" style="height: 450px;" /><br />
          <p style="float: left; font-size: 24pt; margin-top: 40px; text-align: left;" ref="textbody">
            {{this.item.description}}
          </p>
        </a-row>
      </a-col>
    </a-row>
  </div>
</template>

<style>
#app {
  background-color: #f0f3f5;
  min-height: 100%;
}
.header__nav-link {
  position: relative;
  margin: 0 14px;
  cursor: pointer;
  font-size: 18pt;
  font-style: normal;
  font-weight: 500;
  letter-spacing: .01em;
  color: black;
  line-height: 20px;
}
</style>

<script>
import FingerprintJS from '@fingerprintjs/fingerprintjs';
import { Button } from 'ant-design-vue';
import {getFilters, getPost, getPosts, sendScroll} from "../api/auth";

export default {
  name: 'Home',
  components: {
    Button
  },
  data() {
    return {
      filters: [],
      default_filters: [],
      posts: [],
      item: undefined,
    }
  },
  methods: {
    toAuth(e) {
      this.$router.push('/auth')
    }
  },
  mounted() {
    (async () => {
      const fp = await FingerprintJS.load();
      const result = await fp.get();
      const visitorId = result.visitorId;
      console.log(visitorId);

      localStorage.setItem('session', visitorId);
    })();

    (async () => {
      this.item = (await getPost(this.$route.query.id)).posts;

      sendScroll({
        "id_post": this.item.id,
        "percent": 0,
        "type": "place"
      })
      console.log(this.item);
      var check0 = false;
      var check30 = false;
      var check70 = false;
      var check100 = false;

      var hasVerticalScrollbar = this.item.len > 1000;
      if (hasVerticalScrollbar === false) {
        sendScroll({
          "id_post": this.item.id,
          "percent": 100,
          "type": "place"
        })
      }

      window.addEventListener('scroll', function(e){
        var scrollPos = window.scrollY
        var winHeight = window.innerHeight
        var docHeight = document.documentElement.scrollHeight
        var perc = 100 * scrollPos / (docHeight - winHeight);
        console.log(localStorage.getItem('session'));
        if (perc > 0 && perc < 20 && check0 === false) {
          check0 = true;
          sendScroll({
            "id_post": this.item.id,
            "percent": 0,
            "type": "place"
          })
        }
        if (perc > 20 && perc < 50 && check30 === false) {
          check30 = true;
          sendScroll({
            "id_post": this.item.id,
            "percent": 30,
            "type": "place"
          })
        }
        if (perc > 60 && perc < 90 && check70 === false) {
          check70 = true;
          sendScroll({
            "id_post": this.item.id,
            "percent": 70,
            "type": "place"
          })
        }
        if (perc > 90  && check100 === false) {
          check100 = true;
          sendScroll({
            "id_post": this.item.id,
            "percent": 100,
            "type": "place"
          })
        }
      })
    })();
  }
}
</script>

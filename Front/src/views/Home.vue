<template>
  <div>
    <header style="height: 80px; background-color: white; box-shadow: 0 2px 3px 1px rgba(0, 0, 0, .2);">
      <img src="../assets/logo_life.png" style="float: left; height: 80px" />
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
          <h1 style="font-size: 42px; float: left; font-weight: bold; margin-top: 40px;">Места</h1>
        </a-row>
        <a-row>
          <a-button style="float: left; background-color: #60d7f2; border-radius: 20px; padding: 0 24px; font-size: 16pt; line-height: 24pt; height: 40px; margin-right: 20px;">
            <a-icon type="control" />
            Фильтры
          </a-button>
        </a-row>
        <a-row style="padding-top: 16px;">
          <!--          <a-select style="float: left; margin-right: 25px; margin-top: 25px; border: 1px solid #60d7f2; width: 440px; font-size: 18pt;" @change="handleChange" v-for="(value, key, index) in this.filters" :defaultValue="this.default_filters === undefined || this.default_filters[key] === undefined  ? key : this.default_filters[key]">-->
          <a-select style="float: left; margin-right: 25px; margin-top: 25px; border: 1px solid #60d7f2; width: 440px; font-size: 18pt;" @change="handleChange" v-for="(value, key, index) in this.filters" :defaultValue="key">
            <a-select-option value="val" v-for="val in value">
              {{ val }}
            </a-select-option>
          </a-select>
        </a-row>
        <a-row style="padding-top: 16px;">
          <a-button style="width: 48%; margin-right: 2%; font-size: 18pt; height: 70px; border-radius: 5px; padding:10px; background-color: #60d7f2;">Сбросить</a-button>
          <a-button style="width: 48%; margin-left: 2%; font-size: 18pt; height: 70px; border-radius: 5px; background-color: #133748; color: white;">Применить</a-button>
        </a-row>
        <a-row style="background-color: #e6e9eb; padding: 36px; margin-top: 24px;">
          <a-card hoverable style="width: 400px; height: 500px; display: inline-block; float: left; margin: 25px;" v-for="post in this.posts">
            <img slot="cover" alt="example" src="../assets/test.jpeg"/>
            <template slot="actions" class="ant-card-actions">
              <a-anchor-link
                  href="https://www.google.com/maps/place/@post.latitude,post.longitude,17z"
                  title="Basic demo with Target"
                  target="_blank"
              />
            </template>
            <a-card-meta :title="post.title" :description="post.description.substring(0, 220) + '...'" style="float: left; text-align: left; font-size: 14pt; max-width: 370px;"></a-card-meta>
          </a-card>
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
// import FingerprintJS from '@fingerprintjs/fingerprintjs-pro'
import { Button } from 'ant-design-vue';
import {getFilters, getPosts} from "../api/auth";

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
      const result = await getFilters();
      console.log(result)
      this.filters = result.filters
      this.default_filters = result.default_filters;
      console.log(this.default_filters);
      console.log(this.default_filters["Категория"]);
      console.log(this.filters);
    })();

    (async () => {
      this.posts = (await getPosts()).posts;
      console.log(this.posts)
    })();

    window.addEventListener('scroll', function(e){
      var scrollPos = window.scrollY
      var winHeight = window.innerHeight
      var docHeight = document.documentElement.scrollHeight
      var perc = 100 * scrollPos / (docHeight - winHeight)
      console.log(perc);
    })

    // FingerprintJS.load({token: 'AGKYboivuTURYfOXsIxP'})
    //     .then(fp => fp.get())
    //     .then(result => console.log(result.visitorId))
  }
}
</script>

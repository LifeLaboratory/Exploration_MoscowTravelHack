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
          <a-button style="float: left; border-radius: 20px; background-color: #f0f3f5; padding: 0 24px; font-size: 16pt; line-height: 24pt; height: 40px;">
            <a-icon type="search" />
            Поиск
          </a-button>
        </a-row>
        <a-row style="background-color: #e6e9eb; padding: 36px; margin-top: 24px;">
          <a-card hoverable style="width: 300px">
            <img slot="cover" alt="example" src="../assets/test.jpeg"/>
            <a-card-meta title="Прогулка с дедушкой Лениным" description="Особенности и тайны зимнего дворца" style="float: left; text-align: left;"></a-card-meta>
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

export default {
  name: 'Home',
  components: {},
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
    })();

    // FingerprintJS.load({token: 'AGKYboivuTURYfOXsIxP'})
    //     .then(fp => fp.get())
    //     .then(result => console.log(result.visitorId))
  }
}
</script>

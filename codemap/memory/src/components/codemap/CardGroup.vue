<template lang="html">
  <div class="">
    <div>
      <div v-for="i in letter_list" class="code-row">
        <div v-for="j in letter_list">
          <el-card class="box-card">
            <div class="">
              {{ j + i }}
            </div>
          </el-card>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'card-group',
  methods: {
    make_cards () {
      console.log('a')
    }
  },
  data () {
    return {
      letter_list: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    }
  }
}
</script>

<style lang="css">
.code-row {
  display: inline-block;
}
.el-card {
  width: 60px
}
</style>

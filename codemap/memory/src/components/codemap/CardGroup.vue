<template lang="html">
  <div class="">
    <div v-if="data_map">
      <div v-for="i in letter_list" class="code-row">
        <div v-for="j in letter_list">

          <el-card>
            <div class="">
              {{ j + i }}
              <!-- <div v-if="data_map[j + i]" style="display: inline-block;">
              {{data_map[j + i][0].content[0]}}
            </div> -->
          </div>
        </el-card>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'card-group',
  methods: {
    get_data () {
      let self = this
      axios.get('/codemap/build_map/').then((response) => {
        console.log(response)
        if (response.data.status === 'success') {
          self.data_map = response.data.data
          console.log(this.data_map)
        }
      })
    }
  },
  data () {
    return {
      data_map: {},
      letter_list: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    }
  },
  created () {
    this.get_data()
  }
}
</script>

<style lang="css">
.el-card {
  width: 60px;
  border: 1px solid #d1dbe5;
  border-radius: 0px;
  background-color: #fff;
  overflow: hidden;
}
.code-row {
  display: inline-block;
  width: 62px;
}
</style>

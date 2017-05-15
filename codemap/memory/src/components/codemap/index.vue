<template>
  <div class="">
    <div class="">

      success!
      <el-button>默认按钮</el-button>
      <card-group></card-group>
    </div>
  </div>

</template>
<script>
import CardGroup from './CardGroup'

export default {
  name: 'test',
  components: { CardGroup },
  created () {
  }
}
</script>

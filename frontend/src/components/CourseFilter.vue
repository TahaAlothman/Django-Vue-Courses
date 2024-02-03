<template>
  <div class="container">
    <h4>Course Filter</h4>
    <form>
      <div class="mt-3">
        <label for=""  class="mb-3">Filter by Category</label>
      <div v-for="cat in category" :key="cat.id">
        <input type="checkbox"
        :value="cat.id"
        class="form-check-input checkbox-item"
        :id="cat.id"
        v-model="selectedCategory"
        >
        <label :for="cat.id" class="form.label">{{ cat.name }}</label>
      </div>
      </div>
    </form>
  </div>
  
</template>

<script>
  export default {
    name: 'CourseFilter',
    data(){
      return{
        category:[
          {id:1, name:'Web Development'},
          {id:2, name:'Mobile Development'},
          {id:3, name:'AI Development'},
        ],
        selectedCategory:[]
      }
    },
    watch:{
      selectedCategory(){
        this.$emit('category-updated',this.selectedCategory)
      }
    }

  }
</script>
<style>
  .checkbox-item{
    margin-right: 10px;
  }
</style>
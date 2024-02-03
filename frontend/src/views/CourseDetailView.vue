<template>
 <div class="container">
  <div class="row my-5">
    <div class="col-lg-6">
      <img :src="course.image" class="img-fluid" alt="">
    </div>
    <div class="col-lg-6">
      <h2>{{ course.name }}</h2>
      <p>{{ course.category }}</p>
      <p>{{ course.price }}$</p>

      <form method="post" class="row mt-4">
        <div class="col-lg-6">
          <input type="number" value="1" class="form-control">
        </div>
        <div class="col-lg-6">
          <button class="btn btn-info"> Add to Cart</button>
        </div>
      </form>
    </div>
  </div>
 </div>
</template>

<script>
  import { courses } from '../tem-data'
  export default {
    name: 'CourseDetailPage',
    data(){
      return{ 
        course: courses.find(course => course.id == this.$route.params.course_id)//geh zum kurs,deren id sich in url befindet
        
      }
    }
  }
</script>


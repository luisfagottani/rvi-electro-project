<template>
  <div class="canvas" v-bind:style="{ width: this.videoDimensions.widthVideo + 'px', height: this.videoDimensions.heightVideo + 'px'}">
    <canvas id="canvas_paint"></canvas>
    <ul class="panel_edit">
      <!-- <a @click="addSpot()" :class="['add-spot', {remove: addSpotStatus}, {remove: deleteSpotStatus }]">
        <div class="corner">+</div>
        <span class="title">Adicionar Vaga</span>
      </a>
      <a @click="cancelAddSpot()" :class="['edit-spot', {show: addSpotStatus}]">
        <div class="corner"> X </div>
        <span class="title">Cancelar</span>
      </a> -->

      <a @click="excludeSpot()" :class="['edit-spot', {show: deleteSpotStatus}]">
        <div class="corner"> X </div>
        <span class="title" >Excluir Vaga</span>
      </a>
    </ul>
  </div>
</template>

<script>
require("fabric");

export default {
  name: "CanvasPaint",
  props: ["cameraData", "videoDimensions"],
  data() {
    return {
      canvas: "",
      polygonMode: false,
      pointArray: [],
      lineArray: [],
      activeLine: "",
      activeShape: false,
      addSpotStatus: false,
      deleteSpotStatus: false,
      idSpot: 0,
      spots: []
    };
  },
  mounted() {
    var self = this;
    this.canvas = new fabric.Canvas("canvas_paint");
    this.canvas.selection = false;
    this.clickCanvas();
    this.mouseMove();
    this.mouseSelects();

    if (this.cameraData) {
      this.populateSpots();
    }

    this.canvas.forEachObject(function(o) {
      o.selectable = false;
    });
  },
  methods: {
    addPoint: function(options) {
      /**
       * Declarador de variaveis e inclusão de um id temporário, que será usado
       * para verificar o fechamento do polygono.
       */

      const min = 99;
      const max = 999999;
      const random = Math.floor(Math.random() * (max - min + 1)) + min;
      const id = new Date().getTime() + random;

      /**
       * Cria o objeto Circulo (Representação do ponto no canvas)
       */
      let circle = new fabric.Circle({
        radius: 5,
        fill: "#ffffff",
        stroke: "#333333",
        strokeWidth: 0.5,
        left: options.e.layerX / this.canvas.getZoom(),
        top: options.e.layerY / this.canvas.getZoom(),
        selectable: false,
        hasBorders: false,
        hasControls: false,
        originX: "center",
        originY: "center",
        id: id,
        objectCaching: false
      });

      if (this.pointArray.length == 0) {
        circle.set({
          fill: "blue"
        });
      }

      var points = [
        options.e.layerX / this.canvas.getZoom(),
        options.e.layerY / this.canvas.getZoom(),
        options.e.layerX / this.canvas.getZoom(),
        options.e.layerY / this.canvas.getZoom()
      ];

      let line = new fabric.Line(points, {
        strokeWidth: 2,
        fill: "#999999",
        stroke: "#999999",
        class: "line",
        originX: "center",
        originY: "center",
        selectable: false,
        hasBorders: false,
        hasControls: false,
        evented: false,
        objectCaching: false
      });

      /**
       * Caso já exista mais que um ponto, será criado um objeto que
       * irá pre renderizar como o polygono ficará.
       */
      if (this.activeShape) {
        var pos = this.canvas.getPointer(options.e);
        var points = this.activeShape.get("points");
        points.push({
          x: pos.x,
          y: pos.y
        });
        var polygon = new fabric.Polygon(points, {
          stroke: "#333333",
          strokeWidth: 1,
          fill: "#cccccc",
          opacity: 0.3,
          selectable: false,
          hasBorders: false,
          hasControls: false,
          evented: false,
          objectCaching: false
        });
        this.canvas.remove(this.activeShape);
        this.canvas.add(polygon);
        this.activeShape = polygon;
        this.canvas.renderAll();
      } else {
        var polyPoint = [
          {
            x: options.e.layerX / this.canvas.getZoom(),
            y: options.e.layerY / this.canvas.getZoom()
          }
        ];
        var polygon = new fabric.Polygon(polyPoint, {
          stroke: "#333333",
          strokeWidth: 1,
          fill: "#cccccc",
          opacity: 0.3,
          selectable: false,
          hasBorders: true,
          hasControls: false,
          evented: false,
          objectCaching: false
        });
        this.activeShape = polygon;
        this.canvas.add(polygon);
      }

      this.activeLine = line;

      this.pointArray.push(circle);
      this.lineArray.push(line);

      this.canvas.add(line);
      this.canvas.add(circle);
      this.canvas.selection = false;
    },
    generatePolygon: function(pointArray) {
      var points = new Array();
      var self = this;

      pointArray.forEach(function(point, index) {
        points.push({
          x: point.left,
          y: point.top
        });
        self.canvas.remove(point);
      });

      this.lineArray.forEach(function(line, inex) {
        self.canvas.remove(line);
      });

      this.canvas.remove(this.activeShape).remove(this.activeLine);
      var polygon = new fabric.Polygon(points, {
        stroke: "blue",
        strokeWidth: 1,
        fill: "rgba(0,0,255,0.3)",
        opacity: 1,
        hasBorders: true,
        hasControls: false,
        lockMovementX: true,
        lockMovementY: true
      });

      this.canvas.add(polygon);
      this.idSpot += 1;
      polygon.id = this.idSpot;
      this.saveSpot(polygon);
      this.$emit("spots", this.spots);

      this.activeLine = null;
      this.activeShape = null;
      this.polygonMode = false;
      this.addSpotStatus = false;
      this.pointArray = [];

      this.canvas.forEachObject(function(o) {
        o.selectable = true;
      });
    },
    clickCanvas: function() {
      var self = this;
      this.canvas.on("mouse:down", function(options) {
        if (self.pointArray.length > 2) {
          self.addPoint(options);
          self.generatePolygon(self.pointArray);
        } else {
          if (self.polygonMode) {
            self.addPoint(options);
          }
        }
      });
    },
    mouseMove: function() {
      let canvinhas = this.canvas;
      var self = this;

      this.canvas.on("mouse:move", function(options) {
        if (self.activeLine && self.activeLine.class == "line") {
          var pointer = canvinhas.getPointer(options.e);
          self.activeLine.set({ x2: pointer.x, y2: pointer.y });
          var points = self.activeShape.get("points");

          points[self.pointArray.length] = {
            x: pointer.x,
            y: pointer.y
          };

          self.activeShape.set({
            points: points
          });
          canvinhas.renderAll();
        }
        canvinhas.renderAll();
      });
    },
    mouseSelects: function() {
      var self = this;
      this.canvas.on("selection:created", function(options) {
        self.deleteSpotStatus = true;
      });

      this.canvas.on("selection:cleared", function(options) {
        self.deleteSpotStatus = false;
      });
    },
    addSpot: function() {
      this.canvas.setHeight(this.videoDimensions.heightVideo);
      this.canvas.setWidth(this.videoDimensions.widthVideo);
      this.addSpotStatus = true;
      this.polygonMode = true;
      this.pointArray = new Array();
      this.lineArray = new Array();
      this.activeLine;
      this.canvas.forEachObject(function(o) {
        o.selectable = false;
      });
      this.canvas.discardActiveObject();
      this.canvas.renderAll();
    },
    cancelAddSpot: function() {
      this.canvas.clear();
      this.addSpotStatus = false;
      this.polygonMode = false;
      this.pointArray = new Array();
      this.lineArray = new Array();
      this.activeLine = null;
      this.activeShape = null;

      for (var x = 0; x < this.spots.length; x++) {
        var polygon = new fabric.Polygon(this.spots[x].cords, {
          stroke: "blue",
          strokeWidth: 1,
          fill: "rgba(0,0,255,0.3)",
          opacity: 1,
          hasBorders: true,
          hasControls: false,
          lockMovementX: true,
          lockMovementY: true,
          id: this.spots[x].id
        });
        this.canvas.add(polygon);
      }

      this.canvas.renderAll();
    },
    saveSpot: function(object) {
      var spot = {
        id: object.id,
        status: 0,
        cords: [
          {
            x: object.points[0].x,
            y: object.points[0].y
          },
          {
            x: object.points[1].x,
            y: object.points[1].y
          },
          {
            x: object.points[2].x,
            y: object.points[2].y
          },
          {
            x: object.points[3].x,
            y: object.points[3].y
          }
        ]
      };
      // vagas.push(Object.assign({}, raizObject[x]));
      this.spots.push(spot);
    },

    excludeSpot: function() {
      var spotToRemove = this.canvas.getActiveObject();
      this.canvas.remove(spotToRemove);

      this.spots = this.spots.filter(spot => {
        if (spotToRemove.id === spot.id) {
          return false;
        } else {
          return true;
        }
      });
      this.$emit("spots", this.spots);
    },

    populateSpots: function() {
      this.canvas.clear();
      this.addSpotStatus = false;
      this.polygonMode = false;
      this.pointArray = new Array();
      this.lineArray = new Array();
      this.activeLine = null;
      this.activeShape = null;

      for (var x = 0; x < this.cameraData.length; x++) {
        var polygon = new fabric.Polygon(this.cameraData[x].cords, {
          stroke: "blue",
          strokeWidth: 1,
          fill: "rgba(0,0,255,0.3)",
          opacity: 1,
          hasBorders: true,
          hasControls: false,
          lockMovementX: true,
          lockMovementY: true,
          id: this.cameraData[x].id
        });
        this.canvas.add(polygon);
      }
      this.canvas.renderAll();
    }
  }
};
</script>

<style lang="scss" scoped>
.canvas {
  position: absolute !important;
  left: 0;
  top: 0;
  z-index: 5;
  margin: 0 auto;
}
.panel_edit {
  padding: 5px;
  float: right;
  display: block;
  position: relative;
  width: 80px;
}
.add-spot {
  position: absolute;
  right: 0px;
  top: 10px;
  z-index: 10;
  text-align: center;
  transition: 0.3s ease-in-out all;
  width: 80px;
}

.add-spot.remove {
  right: 0px;
  top: 20px;
  opacity: 0;
  visibility: hidden;
}

.add-spot .corner,
.edit-spot .corner {
  display: inline-block;
  width: 45px;
  height: 45px;
  line-height: 35px;
  border-radius: 50px;
  border: 2px solid #fbf7f7;
  background-color: #4286f4;
  color: #ffffff;
  -webkit-box-shadow: 0px 0px 3px 0px rgba(0, 0, 0, 0.75);
  -moz-box-shadow: 0px 0px 3px 0px rgba(0, 0, 0, 0.75);
  box-shadow: 0px 0px 3px 0px rgba(0, 0, 0, 0.75);
  transition: 0.2s ease-in-out all;
  font-size: 38px;
  text-align: center;
}

.add-spot .corner:hover {
  transition: 0.2s ease-in-out all;
  background-color: #2b60b5;
}

.add-spot .title {
  display: block;
  bottom: 0;
  left: 0;
  right: 0;
  margin: 0 auto;
  font-size: 16px;
}

.edit-spot {
  visibility: hidden;
  opacity: 0;
  position: absolute;
  right: 0px;
  top: 10px;
  z-index: 10;
  text-align: center;
  transition: 0.3s ease-in-out all;
  height: 80px;
  width: 80px;
}

.edit-spot.show {
  opacity: 1;
  visibility: visible;
  right: 0;
  top: 10px;
}

.edit-spot .corner {
  background-color: #b91e1e;
  font-size: 23px;
  line-height: 40px;
  font-size: 23px;
  line-height: 40px;
}

.edit-spot .corner:hover {
  background-color: #680d0d;
  cursor: pointer;
}

.add-spot .title,
.edit-spot .title {
  display: block;
  bottom: 0;
  left: 0;
  right: 0;
  margin: 0 auto;
  font-size: 16px;
  color: #ffffff;
  font-weight: bold;
}
</style>

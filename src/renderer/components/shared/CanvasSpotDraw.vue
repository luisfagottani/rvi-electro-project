<template>
  <div class="canvas" v-bind:style="{ width: this.videoDimensions.widthVideo + 'px', height: this.videoDimensions.heightVideo + 'px'}">
    <canvas id="canvas_paint"></canvas>
  </div>
</template>

<script>
require("fabric");
export default {
  name: "CanvasSpotDraw",
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
      spots: [],
      canvasMode: this.$route.query.canvasMode
    };
  },
  mounted() {
    this.init();
  },
  beforeDestroy() {
    this.$store.dispatch("setCanvas", "");
  },
  methods: {
    init() {
      var self = this;
      this.canvas = new fabric.Canvas("canvas_paint");
      this.canvas.setHeight(this.videoDimensions.heightVideo);
      this.canvas.setWidth(this.videoDimensions.widthVideo);

      this.canvas.selection = false;
      if (this.canvasMode === "edit" || this.canvasMode === "add") {
        this.clickCanvas();
        this.mouseMove();
        this.mouseSelects();
      } else {
        this.canvas.on("selection:created", function(options) {
          self.$emit("idSpot", options.target.id);
        });
      }

      if (this.cameraData && this.cameraData.spots) {
        this.spots = Object.assign([], this.cameraData.spots);
        this.populateSpots();
        this.resizeCanvas();
      } else {
        this.spots = [];
      }
      this.$store.dispatch("setCanvas", this.canvas);
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
    selectCanvasClear: function() {
      this.canvas.discardActiveObject();
    },
    mouseMove: function() {
      const self = this;

      this.canvas.on("mouse:move", function(options) {
        if (self.activeLine && self.activeLine.class == "line") {
          let pointer = self.canvas.getPointer(options.e);
          self.activeLine.set({ x2: pointer.x, y2: pointer.y });
          let points = self.activeShape.get("points");

          points[self.pointArray.length] = {
            x: pointer.x,
            y: pointer.y
          };

          self.activeShape.set({
            points: points
          });
          self.canvas.renderAll();
        }
        self.canvas.renderAll();
      });
    },
    mouseSelects: function() {
      var self = this;
      this.canvas.on("selection:created", function(options) {
        self.deleteSpotStatus = true;
        self.$emit("showRemoveCta", self.deleteSpotStatus);
      });

      this.canvas.on("selection:cleared", function(options) {
        self.deleteSpotStatus = false;
        self.$emit("showRemoveCta", self.deleteSpotStatus);
      });
    },
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
      polygon.id =
        this.spots.length < 1
          ? 1
          : Math.max.apply(
              Math,
              this.spots.map(function(o) {
                return o.id + 1;
              })
            );
      this.saveSpot(polygon);
      this.$emit("showAddSpot", false);

      this.canvas.defaultCursor = "initial";
      this.activeLine = null;
      this.activeShape = null;
      this.polygonMode = false;
      this.addSpotStatus = false;
      this.pointArray = [];

      this.canvas.forEachObject(function(o) {
        o.selectable = true;
      });
    },
    addSpot: function() {
      this.canvas.defaultCursor = "copy";
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
      this.$emit("showAddSpot", true);
    },
    saveSpot(retangularSpot) {
      var spot = {
        id: retangularSpot.id,
        status: 0,
        cords: [
          {
            x: retangularSpot.points[0].x,
            y: retangularSpot.points[0].y
          },
          {
            x: retangularSpot.points[1].x,
            y: retangularSpot.points[1].y
          },
          {
            x: retangularSpot.points[2].x,
            y: retangularSpot.points[2].y
          },
          {
            x: retangularSpot.points[3].x,
            y: retangularSpot.points[3].y
          }
        ]
      };
      this.spots.push(spot);
      this.$emit("spots", this.spots);
    },
    removeSpot(retangularSpot) {
      var spotToRemove = this.canvas.getActiveObject();
      this.canvas.remove(spotToRemove);
      let spotAux = this.spots.findIndex(x => x.id === spotToRemove.id);
      this.spots.splice(spotAux, 1);
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
    resizeCanvas: function() {
      let scaleMultiplier =
        this.videoDimensions.widthVideo / this.cameraData.width;
      const heightVar = this.canvas.getHeight() * scaleMultiplier;
      const widthVar = this.canvas.getWidth() * scaleMultiplier;
      var objects = this.canvas.getObjects();
      for (var i in objects) {
        objects[i].scaleX = objects[i].scaleX * scaleMultiplier;
        objects[i].scaleY = objects[i].scaleY * scaleMultiplier;
        objects[i].left = objects[i].left * scaleMultiplier;
        objects[i].top = objects[i].top * scaleMultiplier;
        objects[i].setCoords();
      }
      var obj = this.canvas.backgroundImage;
      if (obj) {
        obj.scaleX = obj.scaleX * scaleMultiplier;
        obj.scaleY = obj.scaleY * scaleMultiplier;
      }

      this.canvas.discardActiveObject();
      this.canvas.setWidth(parseInt(widthVar));
      this.canvas.setHeight(parseInt(heightVar));
      this.canvas.renderAll();
      this.canvas.calcOffset();
    },
    cancelAddSpot: function() {
      this.canvas.defaultCursor = "initial";
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
</style>

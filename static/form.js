const CUSTOM_LIST = 0;
const AI_LIST     = 1;
const RANDOM_LIST = 2;

const updatePlaceholder = (type) => {
  let text = "Nothing to see here";

  if (type == CUSTOM_LIST) {
    text = "Enter your list of words, each separated by a new line";
  }

  if (type == AI_LIST) {
    text = "Enter a category (i.e. sports, food, cities, etc.)";
  }

  $("#text").attr("placeholder", text);
  $("#text").show();

  if (type == RANDOM_LIST) {
    $("#text").hide();
  }
};

const updateButtons = (type) => {
  $("#custom-btn").removeClass("green-button");
  $("#custom-btn").addClass("light-green-button");

  $("#ai-btn").removeClass("green-button");
  $("#ai-btn").addClass("light-green-button");

  $("#random-btn").removeClass("green-button");
  $("#random-btn").addClass("light-green-button");

  if (type == CUSTOM_LIST) {
    $("#custom-btn").removeClass("light-green-button");
    $("#custom-btn").addClass("green-button");
  }

  if (type == AI_LIST) {
    $("#ai-btn").removeClass("light-green-button");
    $("#ai-btn").addClass("green-button");
  }

  if (type == RANDOM_LIST) {
    $("#random-btn").removeClass("light-green-button");
    $("#random-btn").addClass("green-button");
  }
};

$(() => {
  updatePlaceholder(CUSTOM_LIST);
});

$("#custom-btn").click(() => {
  $("#type").attr("value", CUSTOM_LIST);
  updatePlaceholder(CUSTOM_LIST);
  updateButtons(CUSTOM_LIST);
});

$("#ai-btn").click(() => {
  $("#type").attr("value", AI_LIST);
  updatePlaceholder(AI_LIST);
  updateButtons(AI_LIST);
});

$("#random-btn").click(() => {
  $("#type").attr("value", RANDOM_LIST);
  updatePlaceholder(RANDOM_LIST);
  updateButtons(RANDOM_LIST);
});

$(".error-message > button").click((event) => {
  event.preventDefault();

  const messageDiv = $(event.target).parent();
  $(messageDiv).hide();
});

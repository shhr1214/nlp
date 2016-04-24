(ns ch1
  (:require [clojure.string :as s]))

;; 01
(defn reverse-string [str]
  (s/reverse str))

;; 02
(defn extract-string [s1]
  (apply str (take-nth 2 s1)))

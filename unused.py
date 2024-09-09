# def find_best_label_propagation_model(complete_df, missing_values_df, preprocessor):
#     X_labeled = complete_df.drop("label", axis=1)
#     y_labeled = complete_df["label"]
    
#     encoder = LabelEncoder()
#     y_encoded = encoder.fit_transform(y_labeled)

#     X_train, X_test, y_train, y_test = train_test_split(X_labeled, y_encoded, test_size=0.3, random_state=42)

#     X_unlabeled = missing_values_df.drop("label", axis=1)

#     X_combined = pd.concat([X_train, X_unlabeled], axis=0)
#     y_combined = pd.concat([pd.Series(y_train), pd.Series([-1] * len(X_unlabeled))])

#     label_propagation = LabelPropagation()

#     pipeline = create_sklearn_pipeline(preprocessor, label_propagation)

#     pipeline.fit(X_combined, y_combined)
    
#     pseudo_labels = pipeline.named_steps['model'].transduction_[len(X_train):]
#     X_unlabeled['pseudo_label'] = pseudo_labels

#     y_pred_test = pipeline.predict(X_test)

#     y_test_decoded = encoder.inverse_transform(y_test)
#     y_pred_test_decoded = encoder.inverse_transform(y_pred_test)


#     print("Classification Report:")
#     print(classification_report(y_test_decoded, y_pred_test_decoded))

#     accuracy = accuracy_score(y_test_decoded, y_pred_test_decoded)
#     print(f"Accuracy on Test Set: {accuracy:.2f}")

#     return X_unlabeled, accuracy